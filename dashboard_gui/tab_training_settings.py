from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTabWidget
from update_configs import parse_arguments_from_class

class TrainingSettingsTab(QWidget):
    def __init__(self, args_info):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.inputs = {}

        for arg, info in args_info.items():
            self.add_parameter_setting(arg, info)

        self.saveButton = QPushButton("Save Training Settings")
        self.saveButton.clicked.connect(self.save_settings)
        self.layout.addWidget(self.saveButton)

        self.reloadButton = QPushButton("Reload Training Settings")
        self.reloadButton.clicked.connect(self.reload_settings)
        self.layout.addWidget(self.reloadButton)

    def add_parameter_setting(self, arg, info):
        hbox = QHBoxLayout()
        label = QLabel(f"{info['label']}:")
        widget = QLineEdit(str(info['default'])) if info['type'] in ['int', 'float', 'str'] else QComboBox()
        if isinstance(widget, QComboBox):
            widget.addItems(['True', 'False'])  # Simplified assumption; customize based on real types
            widget.setCurrentText(str(info['default']))
        hbox.addWidget(label)
        hbox.addWidget(widget)
        self.layout.addLayout(hbox)
        self.inputs[arg] = widget

    def save_settings(self):
        settings = {arg: widget.text() for arg, widget in self.inputs.items()}
        with open('training_settings.json', 'w') as f:
            json.dump(settings, f, indent=4)

    def reload_settings(self):
        with open('training_settings.json', 'r') as f:
            settings = json.load(f)
        for arg, widget in self.inputs.items():
            widget.setText(str(settings.get(arg)))
