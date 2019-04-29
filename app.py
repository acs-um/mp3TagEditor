from PyQt5.QtCore import QVariant, Qt, QAbstractTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView
from Source.mainWindows import Ui_MainWindow
import os


class ListFileModel(QAbstractTableModel):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items
        self.refresh()

    def refresh(self):
        self.layoutAboutToBeChanged.emit()
        self.layoutChanged.emit()
        self.modelReset.emit()

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.items)

    def columnCount(self, parent=None, *args, **kwargs):
        return 1

    def data(self, QModelIndex, role=None):
        if not QModelIndex.isValid():
            return QVariant()

        if role != Qt.DisplayRole:
            return QVariant()

        data = self.items[QModelIndex.row()].name
        return data

    def headerData(self, p_int, Qt_Orientation, role=None):
        return QVariant('Nombre')


class ListFile:
    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1:][0]


class MainWindows(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):  # Constructor de la clase
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.itemsList = []
        self.listModel = ListFileModel(self.itemsList, parent=self)
        self.tableView.setModel(self.listModel)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnAddListMenu.triggered.connect(self.add_to_list)
        self.btnAdd.setText("Add Dir")

        self.btnAdd.clicked.connect(self.add_folder_to_list)
        # double click (itemActivated)
        # self.listView.itemActivated.connect(self.play_from_playlist)
        # itemClicked es con un solo click
        # self.listWidget.itemClicked.connect(self.stop_song)

    def add_to_list(self):
        path = QFileDialog.getOpenFileName(self, "Choose mp3 file", os.path.expanduser('~/Música/Doom OST'),
                                           "All Files (*);;mp3 Files (*.mp3)")
        if path[0].endswith('mp3'):
            list_file = ListFile(path[0])
            self.listModel.items.append(list_file)
            self.listModel.refresh()
        else:
            # Crear un cartel que no deje agregar archivos no mp3
            print("Archivo no mp3")

    def remove_from_list(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def add_folder_to_list(self):
        folder = QFileDialog.getExistingDirectory(self, "Choose folder", os.path.expanduser('~/Música/DOOM OST'))
        if folder:
            folder_list = os.listdir(folder)
            items = []
            for file in folder_list:
                if file.endswith('mp3'):
                    path = os.path.join(folder, file)
                    list_file = ListFile(path)
                    items.append(list_file)
            self.listModel.items.extend(items)
            self.listModel.refresh()

    def play_from_playlist(self):
        row = self.listWidget.currentRow()
        file = self.listWidget.item(row).text()
        # play_pause(file)


if __name__ == "__main__":
    app = QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()
