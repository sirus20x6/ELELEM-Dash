# main_application.py
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from config_parser import load_and_parse_ast

class MainApplication(QMainWindow):
    def __init__(self, all_settings):
        super().__init__()
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        for category, settings in all_settings.items():
            tab = SettingsTab(category, settings)
            self.tabs.addTab(tab, category)
