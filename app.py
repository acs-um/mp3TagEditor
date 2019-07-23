from PyQt5 import QtWidgets, QtCore

import sys
import os
import eyed3
import io

from PyQt5.QtWidgets import QFileDialog, QHeaderView, QShortcut, QDialog, QPushButton
from PyQt5.QtGui import QPixmap, QKeySequence
from Source.mainWindows import Ui_MainWindow
from Source.MediaPlayer import MediaPlayer
from Source.PlayList import PlayList
from Source.table_models import ListFileModel
from PIL import Image, ImageQt

AUDIO_PATH = os.path.expanduser('~')


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.volume = 80
        self.mediaPlayer = MediaPlayer()
        self.mediaPlayer.set_volume(self.volume)
        self.volumeSlider.setValue(self.volume)
        self.volumeSlider.valueChanged.connect(self.mediaPlayer.set_volume)
        self.btnPlay.clicked.connect(self.play_pause)
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
        if not self.listModel.rowCount():
            return 0
        index = self.tableView.selectedIndexes()[0]
        path = self.playList.get_path_from_list(index)
        self.mediaPlayer.set_path(path)
        self.mediaPlayer.play()
        self.load_info(path)

    def play_pause(self):
        try:
            self.double_click()
        except IndexError:
            if not self.listModel.rowCount():
                self.add_to_list()
            else:
                self.show_dialog()

    def show_dialog(self):
        dialog = Dialog(self)
        dialog.show()

    def load_info(self, file):
        audiofile = eyed3.load(file)
        audio = audiofile.tag

        self.titleEdit.setText(audio.title)
        self.artistEdit.setText(audio.artist)
        self.albumEdit.setText(audio.album)

        try:
            r_year = audio.recording_date.year
            if r_year:
                format_year = "{}".format(r_year)
                self.yearEdit.setText(format_year)
            else:
                self.yearEdit.setText('')
        except AttributeError:
            self.yearEdit.setText('')

        format_track = "{}/{}".format(audio.track_num[0], audio.track_num[1])
        self.trackEdit.setText(format_track)

        format_genre = "{}".format(audio.genre)
        genre = format_genre.split(")")[-1:][0]
        self.genreEdit.setText(genre)

        self.composerEdit.setText(audio.composer)

        comment = audio.comments.get('description')
        if comment:
            self.commentEdit.setText(comment)

        img_b = audio.images.get('')
        if img_b:
            image = Image.open(io.BytesIO(img_b.image_data))
            q_img = ImageQt.ImageQt(image)
            pixmap = QPixmap.fromImage(q_img)
            self.imgCover.setPixmap(pixmap)
        else:
            self.imgCover.setPixmap(QPixmap(":/iconos/images/default_cover.png"))


class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("MP3 Editor - Reproducir")
        self.setFixedSize(400, 200)
        self.lblDialog = QtWidgets.QLabel(self)
        self.lblDialog.setText("Debe seleccionar de la lista para poder reproducir")
        self.btnAccept = QtWidgets.QPushButton(self)
        self.btnAccept.setText("Aceptar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec_())
