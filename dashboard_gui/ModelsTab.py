import sys
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QComboBox, QFileDialog)

class ModelsTab(QWidget):
    def __init__(self, settings_file="models_settings.json"):
        super().__init__()
        self.settings_file = settings_file
        self.layout = QVBoxLayout(self)

        self.settings = {
            "model_path": {"type": "input", "default": ""},
            "model_type": {"type": "dropdown", "options": ["PreTrained", "TFPreTrained", "FlaxPreTrained"], "default": "PreTrained"},
            "action": {"type": "dropdown", "options": ["Load Model", "Resize Embeddings", "Prune Heads", "Push to Hub"], "default": "Load Model"}
        }

        self.inputs = {}
        for key, setting in self.settings.items():
            self.add_setting(key, setting)

        self.runButton = QPushButton("Run Action")
        self.runButton.clicked.connect(self.run_action)
        self.layout.addWidget(self.runButton)

        self.loadButton = QPushButton("Load Model")
        self.loadButton.clicked.connect(self.load_model)
        self.layout.addWidget(self.loadButton)

        self.save_settings_button = QPushButton("Save Settings")
        self.save_settings_button.clicked.connect(self.save_settings)
        self.layout.addWidget(self.save_settings_button)

        self.load_settings()

    def add_setting(self, key, setting):
        hbox = QHBoxLayout()
        label = QLabel(f"{key.replace('_', ' ').capitalize()}:")
        if setting['type'] == 'input':
            widget = QLineEdit(str(setting['default']))
        elif setting['type'] == 'dropdown':
            widget = QComboBox()
            widget.addItems(setting['options'])
            widget.setCurrentText(setting['default'])
        hbox.addWidget(label)
        hbox.addWidget(widget)
        self.layout.addLayout(hbox)
        self.inputs[key] = widget

    def run_action(self):
        action = self.inputs['action'].currentText()
        model_path = self.inputs['model_path'].text()
        # This is a placeholder for actions, implement the functionality as needed
        print(f"Action: {action}, Model Path: {model_path}")

    def load_model(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            self.inputs['model_path'].setText(fname[0])

    def save_settings(self):
        settings_data = {}
        for key, widget in self.inputs.items():
            if isinstance(widget, QLineEdit):
                settings_data[key] = widget.text()
            elif isinstance(widget, QComboBox):
                settings_data[key] = widget.currentText()
        with open(self.settings_file, 'w') as f:
            json.dump(settings_data, f, indent=4)
        print("Model settings saved.")

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as f:
                settings_data = json.load(f)
            for key, value in settings_data.items():
                widget = self.inputs[key]
                if isinstance(widget, QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, QComboBox):
                    widget.setCurrentText(value)
        except FileNotFoundError:
            print("Model settings file not found, using defaults.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModelsTab()
    ex.show()
    sys.exit(app.exec_())
