from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog
import json

class ModelInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.loadModelButton = QPushButton("Load Model")
        self.loadModelButton.clicked.connect(self.load_model)
        self.modelLabel = QLabel("No model loaded.")
        self.settingsLayout = QVBoxLayout()  # Layout for adding settings

        layout.addWidget(self.loadModelButton)
        layout.addWidget(self.modelLabel)
        layout.addLayout(self.settingsLayout)

    def load_model(self):
        # Open a dialog to choose the directory
        folder_path = QFileDialog.getExistingDirectory(self, "Select Model Folder")
        if folder_path:
            self.load_configurations(folder_path)

    def load_configurations(self, folder_path):
        try:
            # Load config.json
            with open(f"{folder_path}/config.json", 'r') as file:
                config_data = json.load(file)
            # Load model.safetensors.index.json
            with open(f"{folder_path}/model.safetensors.index.json", 'r') as file:
                model_data = json.load(file)

            # Display the configurations
            self.modelLabel.setText(f"Loaded model from {folder_path}")
            self.show_settings(config_data, model_data)
        except Exception as e:
            self.modelLabel.setText(f"Error loading model: {e}")

    def show_settings(self, config_data, model_data):
        # Clear previous settings
        while self.settingsLayout.count():
            item = self.settingsLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Create editable fields for config data
        for key, value in config_data.items():
            label = QLabel(f"{key}:")
            line_edit = QLineEdit(str(value))
            self.settingsLayout.addWidget(label)
            self.settingsLayout.addWidget(line_edit)

        # Optionally handle model data similarly

