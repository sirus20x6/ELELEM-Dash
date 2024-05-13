# TrainingTab.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from .ConfigurationTab import ConfigurationTab
from .LoggingTab import LoggingTab
from .ModelConfigurationTab import ModelConfigurationTab
from .OptimizationTab import OptimizationTab
from .PipelinesTab import PipelinesTab
from .TrainerTab import TrainerTab
from .tab_data_management import DataManagementTab
from .tab_model_info import ModelInfoTab
from .tab_graphs import GraphsTab

class TrainingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        tab_widget = QTabWidget()


        tab_widget.addTab(DataManagementTab(), "DataManagement")
        tab_widget.addTab(ConfigurationTab(), "Configuration")
        tab_widget.addTab(LoggingTab(), "Logging")
        tab_widget.addTab(ModelInfoTab(), "Model Info")
        tab_widget.addTab(ModelConfigurationTab(), "Models")
        tab_widget.addTab(OptimizationTab(), "Optimization")
        tab_widget.addTab(PipelinesTab(), "Pipelines")
        tab_widget.addTab(TrainerTab(), "Trainer")
        tab_widget.addTab(GraphsTab(), "Graphs")
        layout.addWidget(tab_widget)
        self.setLayout(layout)
