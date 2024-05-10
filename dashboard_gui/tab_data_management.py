from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox

class DataManagementTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Example Checkbox
        checkBox = QCheckBox("Dataset 1")
        layout.addWidget(checkBox)
