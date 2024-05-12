from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from .gui_utils import SettingsTab

class OptimizationTab(QWidget, SettingsTab):
    def __init__(self, settings_file="optimization_settings.json"):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.settings_file = settings_file
        self.init_settings()
        self.initUI()

    def init_settings(self):
        self.settings = {
            "optimizer": {"type": "dropdown", "options": ["AdamW", "AdaFactor"], "default": "AdamW"},
            "lr": {"type": "input", "default": "0.001"},
            "weight_decay": {"type": "input", "default": "0.01"},
            "eps": {"type": "input", "default": "1e-06"},
            "schedule": {"type": "dropdown", "options": ["Constant", "Cosine", "Linear"], "default": "Constant"}
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
