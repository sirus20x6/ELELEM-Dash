# TrainingTab.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from .ConfigurationTab import ConfigurationTab
from .LoggingTab import LoggingTab
from .ModelsTab import ModelsTab
from .OptimizationTab import OptimizationTab
from .ModelOutputsTab import ModelOutputsTab
from .PipelinesTab import PipelinesTab
from .ProcessorsTab import ProcessorsTab
from .TokenizerTab import TokenizerTab
from .TrainerTab import TrainerTab

class TrainingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        tab_widget = QTabWidget()

        tab_widget.addTab(ConfigurationTab(), "Configuration")
        tab_widget.addTab(LoggingTab(), "Logging")
        tab_widget.addTab(ModelsTab(), "Models")
        tab_widget.addTab(OptimizationTab(), "Optimization")
        tab_widget.addTab(ModelOutputsTab(), "Model Outputs")
        tab_widget.addTab(PipelinesTab(), "Pipelines")
        tab_widget.addTab(ProcessorsTab(), "Processors")
        tab_widget.addTab(TokenizerTab(), "Tokenizer")
        tab_widget.addTab(TrainerTab(), "Trainer")

        layout.addWidget(tab_widget)
        self.setLayout(layout)
