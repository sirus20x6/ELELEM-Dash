from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QCheckBox, QComboBox

class SettingsTab:
    def __init__(self):
        self.inputs = {}

    def add_setting(self, layout, key, setting):
        hbox = QHBoxLayout()
        label = QLabel(f"{key.replace('_', ' ').capitalize()}:")
        widget = None

        if setting['type'] == 'input':
            widget = QLineEdit(str(setting['default']))
        elif setting['type'] == 'checkbox':
            widget = QCheckBox()
            widget.setChecked(setting['default'])
        elif setting['type'] == 'dropdown':
            widget = QComboBox()
            for option in setting['options']:
                widget.addItem(option)
            widget.setCurrentText(setting['default'])

        hbox.addWidget(label)
        hbox.addWidget(widget)
        layout.addLayout(hbox)
        self.inputs[key] = widget

    def collect_settings(self):
        collected_settings = {}
        for key, widget in self.inputs.items():
            if isinstance(widget, QCheckBox):
                collected_settings[key] = widget.isChecked()
            elif isinstance(widget, QLineEdit):
                collected_settings[key] = widget.text()
            elif isinstance(widget, QComboBox):
                collected_settings[key] = widget.currentText()
        return collected_settings
