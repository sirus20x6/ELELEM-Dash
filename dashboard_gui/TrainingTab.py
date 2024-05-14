from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from .tabs import ConfigurationTab
from .tabs import LoggingTab
from .tabs import ModelInfoTab
from .tabs import ModelConfigurationTab
from .tabs import PipelinesTab
from .tabs import TrainerTab
from .tab_graphs import GraphsTab
from .tab_data_management import DataManagementTab

class TrainingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        tab_widget = QTabWidget()

        settings_file = "all_settings.json"

        tab_widget.addTab(DataManagementTab(), "DataManagement")
        tab_widget.addTab(ConfigurationTab(settings_file=settings_file), "Configuration")
        tab_widget.addTab(LoggingTab(settings_file=settings_file), "Logging")
        tab_widget.addTab(ModelInfoTab(settings_file=settings_file), "Model Info")
        tab_widget.addTab(ModelConfigurationTab(settings_file=settings_file), "Models")
        tab_widget.addTab(PipelinesTab(settings_file=settings_file), "Pipelines")
        tab_widget.addTab(TrainerTab(settings_file=settings_file), "Trainer")
        tab_widget.addTab(GraphsTab(), "Graphs")
        
        layout.addWidget(tab_widget)
        self.setLayout(layout)

