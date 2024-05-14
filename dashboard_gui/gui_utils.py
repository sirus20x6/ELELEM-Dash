import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QComboBox

class SettingsTab:
    def __init__(self, tab_name, settings_file="all_settings.json"):
        self.inputs = {}
        self.settings_file = settings_file
        self.tab_name = tab_name
        self.load_settings()

    def load_settings(self):
        with open(self.settings_file, 'r') as file:
            all_settings = json.load(file)
            self.settings = all_settings.get(self.tab_name, {})

    def add_setting(self, layout, key, setting):
        hbox = QHBoxLayout()
        label = QLabel(f"{key.replace('_', ' ').capitalize()}:")
        widget = None

        if setting['type'] == 'input':
            widget = QLineEdit(str(setting['default']))
        elif setting['type'] == 'checkbox':
            widget = QCheckBox()
            widget.setChecked(setting['default'])
        elif setting['type'] == 'dropdown':
            widget = QComboBox()
            for option in setting['options']:
                widget.addItem(option)
            widget.setCurrentText(setting['default'])

        hbox.addWidget(label)
        hbox.addWidget(widget)
        layout.addLayout(hbox)
        self.inputs[key] = widget

    def collect_settings(self):
        collected_settings = {}
        for key, widget in self.inputs.items():
            if isinstance(widget, QCheckBox):
                collected_settings[key] = widget.isChecked()
            elif isinstance(widget, QLineEdit):
                collected_settings[key] = widget.text()
            elif isinstance(widget, QComboBox):
                collected_settings[key] = widget.currentText()
        return collected_settings
    
    def load_stylesheet(file_path):
        try:
            with open(file_path, "r") as file:
                stylesheet = file.read()
                return stylesheet
        except IOError as e:
            print(f"Error opening stylesheet file: {e}")
            return ""

