from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QComboBox, QFormLayout
from .gui_utils import SettingsTab

class ConfigurationTab(QWidget):
    def __init__(self, settings_file="all_settings.json"):
        super().__init__()
        self.settings_manager = SettingsTab(tab_name="ConfigurationTab", settings_file=settings_file)
        self.layout = QVBoxLayout(self)
        self.initUI()
        stylesheet = SettingsTab.load_stylesheet("styles.qss")
        self.setStyleSheet(stylesheet)

    def initUI(self):
        # Ensure settings are loaded and exist
        if hasattr(self.settings_manager, 'settings'):
            for key, setting in self.settings_manager.settings.items():
                self.settings_manager.add_setting(self.layout, key, setting)
        else:
            print("Settings could not be loaded")

class LoggingTab(QWidget):
    def __init__(self, settings_file="all_settings.json"):
        super().__init__()
        self.settings_manager = SettingsTab(tab_name="LoggingTab", settings_file=settings_file)
        self.layout = QVBoxLayout(self)
        self.initUI()
        stylesheet = SettingsTab.load_stylesheet("styles.qss")
        self.setStyleSheet(stylesheet)

    def initUI(self):
        # Ensure settings are loaded and exist
        if hasattr(self.settings_manager, 'settings'):
            for key, setting in self.settings_manager.settings.items():
                self.settings_manager.add_setting(self.layout, key, setting)
        else:
            print("Settings could not be loaded")

class ModelInfoTab(QWidget):
    def __init__(self, settings_file="all_settings.json"):
        super().__init__()
        self.settings_manager = SettingsTab(tab_name="ModelInfoTab", settings_file=settings_file)
        self.layout = QVBoxLayout(self)
        self.initUI()
        stylesheet = SettingsTab.load_stylesheet("styles.qss")
        self.setStyleSheet(stylesheet)

    def initUI(self):
        # Ensure settings are loaded and exist
        if hasattr(self.settings_manager, 'settings'):
            for key, setting in self.settings_manager.settings.items():
                self.settings_manager.add_setting(self.layout, key, setting)
        else:
            print("Settings could not be loaded")
            
class ModelConfigurationTab(QWidget):
    def __init__(self, settings_file="all_settings.json"):
        super().__init__()
        self.settings_manager = SettingsTab(tab_name="ModelConfigurationTab", settings_file=settings_file)
        self.layout = QVBoxLayout(self)
        self.initUI()
        stylesheet = SettingsTab.load_stylesheet("styles.qss")
        self.setStyleSheet(stylesheet)

    def initUI(self):
        # Ensure settings are loaded and exist
        if hasattr(self.settings_manager, 'settings'):
            for key, setting in self.settings_manager.settings.items():
                self.settings_manager.add_setting(self.layout, key, setting)
        else:
            print("Settings could not be loaded")
        
            
class PipelinesTab(QWidget,):
    def __init__(self, settings_file="all_settings.json"):
        super().__init__()
        self.settings_manager = SettingsTab(tab_name="PipelinesTab", settings_file=settings_file)
        self.layout = QVBoxLayout(self)
        stylesheet = SettingsTab.load_stylesheet("styles.qss")
        self.setStyleSheet(stylesheet)
        self.initUI()

    def initUI(self):
        # Ensure settings are loaded and exist
        if hasattr(self.settings_manager, 'settings'):
            for key, setting in self.settings_manager.settings.items():
                self.settings_manager.add_setting(self.layout, key, setting)
        else:
            print("Settings could not be loaded")

class TrainerTab(QWidget):
    def __init__(self, settings_file="all_settings.json"):
        super().__init__()
        self.settings_manager = SettingsTab(tab_name="TrainerTab", settings_file=settings_file)
        self.layout = QVBoxLayout(self)
        stylesheet = SettingsTab.load_stylesheet("styles.qss")
        self.setStyleSheet(stylesheet)
        self.initUI()

    def initUI(self):
        # Ensure settings are loaded and exist
        if hasattr(self.settings_manager, 'settings'):
            for key, setting in self.settings_manager.settings.items():
                self.settings_manager.add_setting(self.layout, key, setting)
        else:
            print("Settings could not be loaded")
            
class GraphsTab(QWidget):
    def __init__(self, settings_file="all_settings.json"):
        super().__init__()
        self.settings_manager = SettingsTab(tab_name="GraphsTab", settings_file=settings_file)
        self.layout = QVBoxLayout(self)
        stylesheet = SettingsTab.load_stylesheet("styles.qss")
        self.setStyleSheet(stylesheet)
        self.initUI()

    def initUI(self):
        # Ensure settings are loaded and exist
        if hasattr(self.settings_manager, 'settings'):
            for key, setting in self.settings_manager.settings.items():
                self.settings_manager.add_setting(self.layout, key, setting)
        else:
            print("Settings could not be loaded")