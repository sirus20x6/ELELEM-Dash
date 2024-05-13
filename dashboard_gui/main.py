import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from .TrainingTab import TrainingTab

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
        self.apply_stylesheet()

        training_tab = TrainingTab()
        self.setCentralWidget(training_tab)
        self.show()

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #005599;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #006699;
            }
            QLabel, QLineEdit, QComboBox {
                font-size: 16px;
                padding: 2px;
                margin: 4px;
            }
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QComboBox {
                border: 1px solid #aaa;
                border-radius: 4px;
                padding: 1px 18px 1px 3px;  /* Room for the dropdown arrow */
                min-width: 6em;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid; /* just a single line */
                border-top-right-radius: 3px; /* same radius as the QComboBox */
                border-bottom-right-radius: 3px;
            }
            QComboBox::down-arrow {
                image: url(/path/to/your/image.png); /* Add your path */
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Optional: Apply a dark theme or other QSS here globally
    # import qdarkstyle
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex = MainApp()
    sys.exit(app.exec_())
