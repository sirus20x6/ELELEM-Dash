import sys
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QCheckBox, QComboBox)

class OptimizationTab(QWidget):
    def __init__(self, settings_file="optimization_settings.json"):
        super().__init__()
        self.settings_file = settings_file
        self.layout = QVBoxLayout(self)
        
        self.settings = {
            "optimizer": {"type": "dropdown", "options": ["AdamW", "AdaFactor"], "default": "AdamW"},
            "lr": {"type": "input", "default": "0.001"},
            "weight_decay": {"type": "input", "default": "0.01"},
            "eps": {"type": "input", "default": "1e-06"},
            "schedule": {"type": "dropdown", "options": ["Constant", "Cosine", "Linear"], "default": "Constant"}
        }

        self.inputs = {}
        for key, setting in self.settings.items():
            self.add_setting(key, setting)

        self.saveButton = QPushButton("Save Optimization Settings")
        self.saveButton.clicked.connect(self.save_settings)
        self.layout.addWidget(self.saveButton)
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

    def save_settings(self):
        settings_data = {}
        for key, widget in self.inputs.items():
            if isinstance(widget, QLineEdit):
                settings_data[key] = widget.text()
            elif isinstance(widget, QComboBox):
                settings_data[key] = widget.currentText()
        with open(self.settings_file, 'w') as f:
            json.dump(settings_data, f, indent=4)
        print("Optimization settings saved.")

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
            print("Optimization settings file not found, using defaults.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OptimizationTab()
    ex.show()
    sys.exit(app.exec_())
