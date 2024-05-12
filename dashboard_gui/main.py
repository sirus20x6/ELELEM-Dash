import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from .TrainingTab import TrainingTab

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Transformers Training Dashboard'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 1200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        training_tab = TrainingTab()
        self.setCentralWidget(training_tab)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())
    
    
#        tab_widget.addTab(ModelInfoTab(), "Model Information")
#        tab_widget.addTab(TrainingTab(), "Training Settings")
#        tab_widget.addTab(DataManagementTab(), "Training Data")
#        tab_widget.addTab(GraphsTab(), "Graphs")