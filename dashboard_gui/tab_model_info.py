from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class ModelInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        loadModelButton = QPushButton("Load Model")
        self.modelLabel = QLabel("No model loaded.")

        layout.addWidget(loadModelButton)
        layout.addWidget(self.modelLabel)
