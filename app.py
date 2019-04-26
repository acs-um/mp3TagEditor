from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Source.mainWindows import Ui_MainWindow
import os
import vlc
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
        # doble click (itemActivated)
        self.listWidget.itemActivated.connect(self.playFromPlaylist)
        # itemClicked es con un solo click
        # self.listWidget.itemClicked.connect(self.stopSong)
        # self.btnPlay.clicked.connect(self.playSong)
        self.btnStop.clicked.connect(self.stopSong)
        self.btnRandom.clicked.connect(self.sortList)

    def playSong(self):
      # for song in playlist:
        song = '/home/matias/Música/DOOM OST/Mick Gordon - DOOM ' \
               '(Original Game Soundtrack) (2016) pt. 1/02. Rip & Tear.mp3'
        player = vlc.MediaPlayer(song)
        player.play()

    def stopSong(self):
        pass

    def showItem(self):
        row = self.listWidget.currentRow()
        print(self.listWidget.item(row).text())

    def addToList(self):
        path = QFileDialog.getOpenFileName(self, "Choose mp3 file", os.path.expanduser('~/Música/Doom OST'),
                                           "All Files (*);;mp3 Files (*.mp3)")
        # if path[0].split(".")[-1] == "mp3":
        if path[0].endswith('mp3'):
            list_file = ListFile(path[0])
            self.listWidget.addItem(list_file.path)
        else:
            # Crear un cartel que no deje agregar archivos no mp3
            print("Archivo no mp3")

    def removeFromList(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    # Agrega los nombres y los paths pero medio hardcodeado
    def addFolderToList(self):
        folder = QFileDialog.getExistingDirectory(self, "Choose a folder", os.path.expanduser('~/Música/DOOM OST'))
        if folder:
            folder_list = listdir(folder)
            for file in folder_list:
                if file.endswith('mp3'):
                    path = folder + "/" + file
                    list_file = ListFile(path)
                    self.listWidget.addItem(list_file.path)
        self.listWidget.sortItems()

    def playFromPlaylist(self):
        row = self.listWidget.currentRow()
        song = self.listWidget.item(row).text()
        player = vlc.MediaPlayer(song)
        player.play()
        return player

    def selectedItem(self):
        for i in range(self.listWidget.count()):
            list_file = ListFile(self.listWidget.item(i).text())
            print(list_file.name)

    def sortList(self):
        self.listWidget.sortItems()


if __name__ == "__main__":
    app = QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()

# main = MainWindows()
# list_file = main.addToList
# print(list_file.name)
