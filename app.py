import sys
import os

from Source.Tag import Tag
from PyQt5.QtWidgets import QHeaderView, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5 import QtWidgets
from Source.mainWindows import Ui_MainWindow
from Source.MediaPlayer import MediaPlayer
from Source.PlayList import PlayList
from Source.table_models import ListFileModel
from PIL import Image, ImageQt


AUDIO_PATH = os.path.expanduser('~/Escritorio')


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.volume = 80
        self.mediaPlayer = MediaPlayer()
        self.tag = Tag()
        self.mediaPlayer.set_volume(self.volume)
        self.volumeSlider.setValue(self.volume)
        self.volumeSlider.valueChanged.connect(self.mediaPlayer.set_volume)
        self.btnPlay.clicked.connect(self.mediaPlayer.play_pause)
        self.btnStop.clicked.connect(self.mediaPlayer.stop)
        self.itemsList = []
        self.listModel = ListFileModel(self.itemsList, parent=self)
        self.playList = PlayList(self.listModel)
        self.tableView.setModel(self.listModel)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.doubleClicked.connect(self.double_click)
        self.btnAddListMenu.triggered.connect(self.playList.add_to_list_action)
        self.btnAddFolderListMenu.triggered.connect(self.playList.add_folder_to_list_action)
        self.shortcut = QShortcut(QKeySequence("Delete"), self)
        self.shortcut.activated.connect(self.playList.remove_from_list)

    def double_click(self):
        index = self.tableView.selectedIndexes()[0]
        path = self.playList.get_path_from_list(index)
        self.mediaPlayer.set_path(path)
        self.mediaPlayer.play_pause()
        self.load_info(path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec_())
