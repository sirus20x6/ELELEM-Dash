import sys
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QCheckBox)

class TrainerTab(QWidget):
    def __init__(self, settings_file="trainer_settings.json"):
        super().__init__()
        self.settings_file = settings_file
        self.layout = QVBoxLayout(self)
        self.settings = {
            "output_dir": {"type": "input", "default": "./model_output"},
            "do_train": {"type": "checkbox", "default": False},
            "do_eval": {"type": "checkbox", "default": False},
            "num_train_epochs": {"type": "input", "default": "3"},
            "per_device_train_batch_size": {"type": "input", "default": "8"},
            "per_device_eval_batch_size": {"type": "input", "default": "8"},
            "warmup_steps": {"type": "input", "default": "500"},
            "learning_rate": {"type": "input", "default": "5e-5"},
            "weight_decay": {"type": "input", "default": "0.01"},
            "adam_beta1": {"type": "input", "default": "0.9"},
            "adam_beta2": {"type": "input", "default": "0.999"},
            "adam_epsilon": {"type": "input", "default": "1e-8"},
            "max_grad_norm": {"type": "input", "default": "1.0"}
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
            widget = QLineEdit(str(setting['default']))
        elif setting['type'] == 'checkbox':
            widget = QCheckBox()
            widget.setChecked(setting['default'])
        hbox.addWidget(label)
        hbox.addWidget(widget)
        self.layout.addLayout(hbox)
        self.inputs[key] = widget

    def save_settings(self):
        settings_data = {}
        for key, widget in self.inputs.items():
            if isinstance(widget, QLineEdit):
                settings_data[key] = widget.text()
            elif isinstance(widget, QCheckBox):
                settings_data[key] = widget.isChecked()
        with open(self.settings_file, 'w') as f:
            json.dump(settings_data, f, indent=4)
        print("Settings saved.")

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as f:
                settings_data = json.load(f)
            for key, value in settings_data.items():
                widget = self.inputs[key]
                if isinstance(widget, QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, QCheckBox):
                    widget.setChecked(value)
        except FileNotFoundError:
            print("Settings file not found, using defaults.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TrainerTab()
    ex.show()
    sys.exit(app.exec_())
