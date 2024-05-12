from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from .gui_utils import SettingsTab

class TrainerTab(QWidget, SettingsTab):
    def __init__(self, settings_file="trainer_settings.json"):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.settings_file = settings_file
        self.init_settings()
        self.initUI()

    def init_settings(self):
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
