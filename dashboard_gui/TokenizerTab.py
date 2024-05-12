import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QComboBox

class TokenizerTab(QWidget):
    def __init__(self, settings_file="tokenizer_settings.json"):
        super().__init__()
        self.settings_file = settings_file
        self.layout = QVBoxLayout(self)
        self.settings = {
            "tokenizer_path": {"type": "input", "default": ""},
            "special_tokens": {"type": "input", "default": ""},
            "max_length": {"type": "input", "default": "512"}
        }

        self.inputs = {}
        for key, setting in self.settings.items():
            self.add_setting(key, setting)

        self.saveButton = QPushButton("Save Settings")
        self.saveButton.clicked.connect(self.save_settings)
        self.layout.addWidget(self.saveButton)
        self.load_settings()

    def add_setting(self, key, setting):
        hbox = QHBoxLayout()
        label = QLabel(f"{key.replace('_', ' ').capitalize()}:")
        if setting['type'] == 'input':
            widget = QLineEdit(setting['default'])
        elif setting['type'] == 'dropdown':
            widget = QComboBox()
            widget.addItems(setting['options'])
            widget.setCurrentText(setting['default'])
        hbox.addWidget(label)
        hbox.addWidget(widget)
        self.layout.addLayout(hbox)
        self.inputs[key] = widget

    def save_settings(self):
        settings_data = {key: self.inputs[key].text() if isinstance(self.inputs[key], QLineEdit) else self.inputs[key].currentText() for key in self.inputs}
        with open(self.settings_file, 'w') as f:
            json.dump(settings_data, f, indent=4)
        print("Settings saved.")

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as f:
                settings_data = json.load(f)
            for key, value in settings_data.items():
                if isinstance(self.inputs[key], QComboBox):
                    self.inputs[key].setCurrentText(value)
                else:
                    self.inputs[key].setText(value)
        except FileNotFoundError:
            print("Settings file not found, using defaults.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TokenizerTab()
    ex.show()
    sys.exit(app.exec_())
