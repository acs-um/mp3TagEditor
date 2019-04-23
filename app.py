from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Source.mainWindows import Ui_MainWindow
import os


class ListFile:

    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1:][0]


class MainWindows(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):  # Constructor de la clase
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnAddListMenu.triggered.connect(self.addToList)
        self.btnAdd.clicked.connect(self.addToList)

    def addToList(self):
        path = QFileDialog.getOpenFileName(self, "Choose mp3 file", os.path.expanduser('~/Música'))
        list_file = ListFile(path[0])
        print(list_file.name)
        self.listWidget.addItem(list_file.name)


if __name__ == "__main__":
    app = QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()
