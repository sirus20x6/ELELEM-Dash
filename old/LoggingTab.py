from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from .gui_utils import SettingsTab

class LoggingTab(QWidget, SettingsTab):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.settings_file = "logging_config.json"  # Define the path to your settings file
        self.init_settings()
        self.initUI()

    def init_settings(self):
        self.settings = {
            "verbosity": {"type": "dropdown", "options": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], "default": "WARNING"},
            "progress_bar": {"type": "dropdown", "options": ["enabled", "disabled"], "default": "enabled"},
            "formatting": {"type": "dropdown", "options": ["default", "explicit"], "default": "default"}
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

