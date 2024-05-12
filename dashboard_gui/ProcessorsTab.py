import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QHBoxLayout

class ProcessorsTab(QWidget):
    def __init__(self, settings_file="processor_settings.json"):
        super().__init__()
        self.settings_file = settings_file
        self.layout = QVBoxLayout(self)
        self.processor_type = QComboBox()
        self.processor_type.addItems(["Multi-modal Processor", "Deprecated Processor"])
        self.processor_type.currentIndexChanged.connect(self.update_processor_options)
        self.layout.addWidget(self.processor_type)

        self.options_layout = QVBoxLayout()
        self.layout.addLayout(self.options_layout)
        self.processor_settings = {
            "Multi-modal Processor": {
                "model": {"label": "Model Path", "widget": QLineEdit()},
                "tokenizer": {"label": "Tokenizer Path", "widget": QLineEdit()}
            },
            "Deprecated Processor": {
                "data_directory": {"label": "Data Directory", "widget": QLineEdit()}
            }
        }
        self.load_settings()

        self.save_button = QPushButton("Save Processor Settings")
        self.save_button.clicked.connect(self.save_settings)
        self.layout.addWidget(self.save_button)
        self.update_processor_options(self.processor_type.currentIndex())

    def update_processor_options(self, index):
        # Clear current settings
        for i in reversed(range(self.options_layout.count())): 
            self.options_layout.itemAt(i).widget().setParent(None)

        # Get current processor type
        processor_type = self.processor_type.currentText()
        settings = self.processor_settings[processor_type]

        # Add new settings widgets
        for setting, config in settings.items():
            row = QHBoxLayout()
            row.addWidget(QLabel(config["label"]))
            row.addWidget(config["widget"])
            self.options_layout.addLayout(row)

    def save_settings(self):
        processor_type = self.processor_type.currentText()
        settings = self.processor_settings[processor_type]
        settings_data = {key: config["widget"].text() for key, config in settings.items()}
        with open(self.settings_file, 'w') as file:
            json.dump(settings_data, file, indent=4)
        print("Processor settings saved.")

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as file:
                settings_data = json.load(file)
            processor_type = self.processor_type.currentText()
            settings = self.processor_settings[processor_type]
            for key, value in settings_data.items():
                if key in settings:
                    settings[key]["widget"].setText(value)
        except FileNotFoundError:
            print("Settings file not found. Using defaults.")

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ex = ProcessorsTab()
    ex.show()
    sys.exit(app.exec_())
