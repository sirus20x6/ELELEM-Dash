import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from .TrainingTab import TrainingTab
from .gui_utils import SettingsTab

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Transformers Training Dashboard'
        self.left = 100
        self.top = 100
        self.width = 900
        self.height = 600  # Adjusted for better proportionality
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        stylesheet = SettingsTab.load_stylesheet("styles.qss")
        self.setStyleSheet(stylesheet)
        training_tab = TrainingTab()
        self.setCentralWidget(training_tab)
        self.show()
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Optional: Apply a dark theme or other QSS here globally
    # import qdarkstyle
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex = MainApp()
    sys.exit(app.exec_())
