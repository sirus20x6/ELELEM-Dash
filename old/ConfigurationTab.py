from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from ..dashboard_gui.gui_utils import SettingsTab

class ConfigurationTab(QWidget, SettingsTab):
    def __init__(self, settings_file="config_settings.json"):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.settings_file = settings_file
        self.init_settings()
        self.initUI()

    def init_settings(self):
        self.settings = {
                        "output_hidden_states": {"type": "checkbox", "default": False},
            "output_attentions": {"type": "checkbox", "default": False},
            "return_dict": {"type": "checkbox", "default": True},
            "is_encoder_decoder": {"type": "checkbox", "default": False},
            "is_decoder": {"type": "checkbox", "default": False},
            "add_cross_attention": {"type": "checkbox", "default": False},
            "tie_encoder_decoder": {"type": "checkbox", "default": False},
            "vocab_size": {"type": "input", "default": "30522"},
            "hidden_size": {"type": "input", "default": "768"},
            "num_attention_heads": {"type": "input", "default": "12"},
            "num_hidden_layers": {"type": "input", "default": "12"}
        }

    def initUI(self):
        # Add settings widgets
        for key, setting in self.settings.items():
            self.add_setting(self.layout, key, setting)

        # Buttons layout
        buttons_layout = QHBoxLayout()
        self.saveButton = QPushButton("Save Configuration", self)
        self.saveButton.clicked.connect(lambda: self.save_settings(self.collect_settings(), self.settings_file))
        buttons_layout.addWidget(self.saveButton)

        self.loadButton = QPushButton("Load Configuration", self)
        self.loadButton.clicked.connect(lambda: self.load_configuration(self.settings_file))
        buttons_layout.addWidget(self.loadButton)

        self.layout.addLayout(buttons_layout)


