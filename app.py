import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView
from Source.mainWindows import Ui_MainWindow
from Source.table_models import ListFileModel, ListFile

AUDIO_PATH = os.path.expanduser('~')


class MainWindows(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):  # Constructor de la clase
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.itemsList = []
        self.listModel = ListFileModel(self.itemsList, parent=self)
        self.tableView.setModel(self.listModel)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.doubleClicked.connect(self.play_from_list)
        self.btnAddListMenu.triggered.connect(self.add_to_list)
        self.btnAdd.setText("Add Dir")
        self.btnAdd.clicked.connect(self.add_folder_to_list)

    def add_to_list(self):
        dialog_txt = "Choose mp3 file"
        options = "All Files (*);;mp3 Files (*.mp3)"
        path = QFileDialog.getOpenFileName(self, dialog_txt, AUDIO_PATH, options)
        if path[0].endswith('mp3'):
            list_file = ListFile(path[0])
            self.listModel.items.append(list_file)
            self.listModel.refresh()

    def remove_from_list(self):
        pass

    def add_folder_to_list(self):
        dialog_txt = "Choose folder"
        folder = QFileDialog.getExistingDirectory(self, dialog_txt, AUDIO_PATH)
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

    def play_from_list(self):
        index = self.tableView.selectedIndexes()[0]
        file = self.listModel.get_path(index)
        # play_pause(file)


if __name__ == "__main__":
    app = QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()
