from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFileSystemModel, QTreeView, QTextEdit, QSplitter
from PyQt5.QtCore import QDir, Qt


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
    
    

class DataManagementTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.training_datasets = []

        self.model = CheckableFileSystemModel('./data')
        self.model.setRootPath('./data')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.model.rootPath))

        self.preview = QTextEdit()
        self.preview.setReadOnly(True)

        self.splitter = QSplitter()
        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.preview)
        self.splitter.setSizes([800, 500])

        self.layout.addWidget(self.splitter)
        #self.model.disconnect()
        self.tree.clicked.connect(self.on_item_clicked)
        #self.model.dataChanged.connect(self.on_item_changed)
        #self.ignore_data_changed = False

                
    def on_item_changed(self, item):
        print("on_item_changed")

            
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

