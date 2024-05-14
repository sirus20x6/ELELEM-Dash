from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFileSystemModel, QTreeView, QTextEdit, QSplitter, QPushButton
from PyQt5.QtCore import QDir, Qt
from torchvision import datasets, transforms
import torch

class MyTreeView(QTreeView):
    def __init__(self, parent=None):
        super(MyTreeView, self).__init__(parent)
        # Assume itemChanged is the signal you might want to disconnect
        self.itemChanged.connect(self.handleItemChanged)

    def handleItemChanged(self, item):
        # Custom handling here
        pass

    def disconnectSignals(self):
        # Disconnect the specific signal
        self.itemChanged.disconnect(self.handleItemChanged)


class CheckableFileSystemModel(QFileSystemModel):
    def __init__(self, rootPath):
        super().__init__()
        self.rootPath = rootPath
        self.checks = {}

    def flags(self, index):
        flags = super().flags(index)
        if index.isValid() and index.column() == 0 and index.parent() == self.index(self.rootPath):
            return flags | Qt.ItemIsUserCheckable
        return flags

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.CheckStateRole and index.column() == 0 and index.parent() == self.index(self.rootPath):
            path = self.filePath(index)
            return self.checks.get(path, Qt.Unchecked)
        return super().data(index, role)

    def setData(self, index, value, role=Qt.CheckStateRole):
        print(self, index, value, role)
        if role == Qt.CheckStateRole and index.column() == 0 and index.parent() == self.index(self.rootPath):
            path = self.filePath(index)
            self.checks[path] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return super().setData(index, value, role)
    
    

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTreeView, QPushButton, QTextEdit, QLineEdit, QSplitter
from PyQt5.QtWidgets import QFileSystemModel
import datasets  # Make sure to install the 'datasets' library from Hugging Face

class DataManagementTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.model = QFileSystemModel()
        self.model.setRootPath('./data')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index('./data'))

        self.preview = QTextEdit()
        self.preview.setReadOnly(True)

        self.splitter = QSplitter()
        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.preview)
        self.splitter.setSizes([800, 500])

        self.dataset_path_input = QLineEdit(self)
        self.dataset_path_input.setPlaceholderText("Enter HuggingFace dataset path")
        self.load_dataset_button = QPushButton("Load From HuggingFace", self)
        self.load_dataset_button.clicked.connect(self.load_dataset_from_huggingface)

        self.layout.addWidget(self.splitter)
        self.layout.addWidget(self.dataset_path_input)
        self.layout.addWidget(self.load_dataset_button)

        self.tree.clicked.connect(self.on_item_clicked)

    def on_item_clicked(self, index):
        file_path = self.model.filePath(index)
        self.preview.setText(open(file_path, 'r').read())

    def load_dataset_from_huggingface(self):
        dataset_path = self.dataset_path_input.text().strip()
        if dataset_path:
            # Assuming dataset_path is in the form 'namespace/dataset_name'
            namespace, dataset_name = dataset_path.split('/')
            hf_dataset = datasets.load_dataset(dataset_name, cache_dir='./data', use_auth_token=True, name=namespace)
            print(f"Dataset {dataset_name} loaded from HuggingFace under namespace {namespace}.")
        else:
            print("Please enter a valid HuggingFace dataset path.")

# Note: You may need to adjust the dataset fetching logic depending on the specific format of the dataset paths and any additional parameters.


            
    def on_item_clicked(self, index):
#        if self.model.isDir(index) and index.parent() == self.model.index(self.model.rootPath):
#            current_state = self.model.data(index, Qt.CheckStateRole)
#            new_state = Qt.Checked if current_state == Qt.Unchecked else Qt.Unchecked
#            self.model.setData(index, new_state, Qt.CheckStateRole)
#            folder_path = self.model.filePath(index)
#            if new_state == Qt.Checked:
#                if folder_path not in self.training_datasets:
#                    self.training_datasets.append(folder_path)
#            else:
#                if folder_path in self.training_datasets:
#                    self.training_datasets.remove(folder_path)
        if self.model.fileInfo(index).isFile():
            file_path = self.model.filePath(index)
            with open(file_path, 'r', encoding='utf-8') as file:
                self.preview.setText(file.read())

