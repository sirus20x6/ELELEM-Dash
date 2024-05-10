import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from tab_model_info import ModelInfoTab
from tab_data_management import DataManagementTab
from tab_graphs import GraphsTab

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Training Dashboard")
        self.setGeometry(100, 100, 800, 600)

        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        tab_widget.addTab(ModelInfoTab(), "Model Information")
        tab_widget.addTab(DataManagementTab(), "Training Data")
        tab_widget.addTab(GraphsTab(), "Graphs")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dashboard()
    ex.show()
    sys.exit(app.exec_())
