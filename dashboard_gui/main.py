import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from tab_model_info import ModelInfoTab
from tab_data_management import DataManagementTab
from tab_training_settings import TrainingSettingsTab
from tab_graphs import GraphsTab

# Ensure you have imported update_configs if it's in a different file
import update_configs

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def create_training_settings_tab(self):
        args_info = update_configs.parse_arguments_from_class('/thearray/git/transformers/src/transformers/training_args.py')
        return TrainingSettingsTab(args_info)

    def initUI(self):
        self.setWindowTitle("Training Dashboard")
        self.setGeometry(100, 100, 1200, 600)

        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        tab_widget.addTab(ModelInfoTab(), "Model Information")
        tab_widget.addTab(self.create_training_settings_tab(), "Training Settings")
        tab_widget.addTab(DataManagementTab(), "Training Data")
        tab_widget.addTab(GraphsTab(), "Graphs")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dashboard()
    ex.show()
    sys.exit(app.exec_())
