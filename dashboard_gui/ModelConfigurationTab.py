from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QComboBox, QFormLayout
from .gui_utils import SettingsTab

class ModelConfigurationTab(QWidget, SettingsTab):
    def __init__(self, settings_file="model_config_settings.json"):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.settings_file = settings_file
        self.init_settings()
        self.initUI()

    def init_settings(self):
        # Settings for models, processors, tokenizers, and model outputs
        self.model_settings = {
            "model_path": {"type": "input", "default": ""},
            "model_type": {"type": "dropdown", "options": ["PreTrained", "TFPreTrained", "FlaxPreTrained"], "default": "PreTrained"}
        }
        self.tokenizer_settings = {
            "tokenizer_path": {"type": "input", "default": ""},
            "special_tokens": {"type": "input", "default": ""},
            "max_length": {"type": "input", "default": "512"}
        }
        self.processor_settings = {
            "Multi-modal Processor": {
                "model": {"label": "Model Path", "widget": QLineEdit()},
                "tokenizer": {"label": "Tokenizer Path", "widget": QLineEdit()}
            },
            "Deprecated Processor": {
                "data_directory": {"label": "Data Directory", "widget": QLineEdit()}
            }
        }
        self.model_output_settings = {
            "output_hidden_states": {"type": "dropdown", "options": ["True", "False"], "default": "False"},
            "output_attentions": {"type": "dropdown", "options": ["True", "False"], "default": "False"},
            "use_cache": {"type": "dropdown", "options": ["True", "False"], "default": "True"}
        }

    def initUI(self):
        # Form layout for static settings
        form_layout = QFormLayout()
        self.add_form_entries(form_layout, self.model_settings)
        self.add_form_entries(form_layout, self.tokenizer_settings)
        self.add_form_entries(form_layout, self.model_output_settings)  # Add model output settings here
        self.layout.addLayout(form_layout)

        # Processor type selection and dynamic forms
        self.processor_type = QComboBox()
        self.processor_type.addItems(self.processor_settings.keys())
        self.processor_type.currentIndexChanged.connect(self.update_processor_options)
        self.layout.addWidget(self.processor_type)

        self.options_layout = QVBoxLayout()
        self.layout.addLayout(self.options_layout)
        self.update_processor_options(0)  # Initialize with the first processor type

        # Buttons for saving and loading
        buttons_layout = QHBoxLayout()
        save_button = QPushButton("Save Configuration", self)
        save_button.clicked.connect(lambda: self.save_settings(self.collect_settings(), self.settings_file))
        buttons_layout.addWidget(save_button)

        load_button = QPushButton("Load Configuration", self)
        load_button.clicked.connect(lambda: self.load_configuration(self.settings_file))
        buttons_layout.addWidget(load_button)

        self.layout.addLayout(buttons_layout)

    def add_form_entries(self, form_layout, settings):
        for key, setting in settings.items():
            if setting['type'] == 'input':
                widget = QLineEdit(setting['default'])
                form_layout.addRow(QLabel(key.replace('_', ' ').capitalize() + ":"), widget)
            elif setting['type'] == 'dropdown':
                widget = QComboBox()
                widget.addItems(setting['options'])
                widget.setCurrentText(setting['default'])
                form_layout.addRow(QLabel(key.replace('_', ' ').capitalize() + ":"), widget)

    def update_processor_options(self, index):
        # Clear existing widgets in options layout
        for i in reversed(range(self.options_layout.count())):
            widget_to_remove = self.options_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)

        # Load new processor settings based on the selected processor type
        processor_type = self.processor_type.currentText()
        settings = self.processor_settings[processor_type]
        for setting_key, setting_value in settings.items():
            label = QLabel(setting_value['label'])
            widget = setting_value['widget']
            self.options_layout.addWidget(label)
            self.options_layout.addWidget(widget)

    def collect_settings(self):
        # Collect settings from all dynamic and static fields
        collected_settings = {}
        # Collect settings from model, tokenizer, and model outputs
        for settings_group in [self.model_settings, self.tokenizer_settings, self.model_output_settings]:
            for setting_key, setting_info in settings_group.items():
                if setting_info['type'] == 'input':
                    collected_settings[setting_key] = setting_info['widget'].text()
                elif setting_info['type'] == 'dropdown':
                    collected_settings[setting_key] = setting_info['widget'].currentText()
        # Collect processor specific settings
        processor_type = self.processor_type.currentText()
        settings = self.processor_settings[processor_type]
        for key, value in settings.items():
            collected_settings[key] = value['widget'].text()

        return collected_settings
