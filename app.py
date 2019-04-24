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
        # Borra con doble click
        self.listWidget.itemClicked.connect(self.removeFromList)
        self.btnPlay.clicked.connect(self.selectedItem)


    def addToList(self):
        path = QFileDialog.getOpenFileName(self, "Choose mp3 file", os.path.expanduser('~/Música/Doom OST'),
                                           "All Files (*);;mp3 Files (*.mp3)")
        if path == ('', ''):
            return
        else:
            if path[0].split(".")[-1] == "mp3":
                list_file = ListFile(path[0])
                self.listWidget.addItem(list_file.name)
                print(list_file.path)
                print(list_file.name)
            else:
                # Crear un cartel que no deje agregar archivos no mp3
                print("Archivo no mp3")

    def removeFromList(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    # Agrega los nombres y los paths pero medio hardcodeadoitemActivated
    def addFolderToList(self):
        folder = QFileDialog.getExistingDirectory(self, "Choose a folder", os.path.expanduser('~/Música/DOOM OST'))
        if folder:
            folder_list = listdir(folder)
            for file in folder_list:
                if file.split(".")[-1] == "mp3":
                    path = folder + "/" + file
                    list_file = ListFile(path)
                    self.listWidget.addItem(list_file.name)

    def playFromPlaylist(self):
        for i in range(self.listWidget.count()):
            if self.listWidget.currentItem():
                print(self.listWidget.item(i).text())

    def selectedItem(self):
        for i in range(self.listWidget.count()):
            list_file = ListFile(self.listWidget.item(i).text())
            print(list_file.name)


if __name__ == "__main__":
    app = QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()
