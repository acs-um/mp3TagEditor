from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Source.mainWindows import Ui_MainWindow
import os
from os import listdir


class ListFile:

    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1:][0]


class MainWindows(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):  # Constructor de la clase
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnAddListMenu.triggered.connect(self.addToList)
        self.btnAdd.setText("Add Dir")
        self.btnAdd.clicked.connect(self.addFolderToList)

    def addToList(self):
        path = QFileDialog.getOpenFileName(self, "Choose mp3 file", os.path.expanduser('~/Música'))
        list_file = ListFile(path[0])
        print(list_file.path)
        self.listWidget.addItem(list_file.name)

    def removeFromList(self):
        pass

    # Agrega los nombres y los paths pero medio hardcodeado
    def addFolderToList(self):
        folder = QFileDialog.getExistingDirectory(self, "Choose a folder", os.path.expanduser('~/Música/DOOM OST'))
        folder_list = listdir(folder)
        for file in folder_list:
            path = folder + "/" + file
            list_file = ListFile(path)
            print(list_file.name)
            print(list_file.path)
            self.listWidget.addItem(list_file.name)

    def playFromPlaylist(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()
