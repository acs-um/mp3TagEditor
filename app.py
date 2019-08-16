import sys
import os
import io

from PyQt5.QtWidgets import QDialog

from Source.Tag import Tag
from PyQt5.QtWidgets import QHeaderView, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5 import QtWidgets
from Source.mainWindows import Ui_MainWindow
from Source.MediaPlayer import MediaPlayer
from Source.AudioFile import AudioFile
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
        self.btnEdit.clicked.connect(self.edit_tag)
        self.btnSave.clicked.connect(self.save_tag)
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

    def load_info(self, path):
        audio = self.tag.get_audio_info(path)
        self.titleEdit.setText(audio.title)
        self.titleEdit.setReadOnly(True)
        self.artistEdit.setText(audio.artist)
        self.artistEdit.setReadOnly(True)
        self.albumEdit.setText(audio.album)
        self.albumEdit.setReadOnly(True)

        try:
            r_year = audio.recording_date.year
            if r_year:
                format_year = "{}".format(r_year)
                self.yearEdit.setText(format_year)
                self.yearEdit.setReadOnly(True)
            else:
                self.yearEdit.setText('')
                self.yearEdit.setReadOnly(True)
        except AttributeError:
            self.yearEdit.setText('')

        if audio.track_num[1]:
            format_track = "{}/{}".format(audio.track_num[0], audio.track_num[1])
        else:
            format_track = "{}".format(audio.track_num[0])

        self.trackEdit.setText(format_track)
        self.trackEdit.setReadOnly(True)

        format_genre = "{}".format(audio.genre)
        genre = format_genre.split(")")[-1:][0]
        self.genreEdit.setText(genre)
        self.genreEdit.setReadOnly(True)

        self.composerEdit.setText(audio.composer)
        self.composerEdit.setReadOnly(True)

        comment = audio.comments.get('description')
        if comment:
            self.commentEdit.setText(comment)

        self.commentEdit.setReadOnly(True)

        img_b = audio.images.get('')
        if img_b:
            image = Image.open(io.BytesIO(img_b.image_data))
            q_img = ImageQt.ImageQt(image)
            pixmap = QPixmap.fromImage(q_img)
            self.imgCover.setPixmap(pixmap)
        else:
            self.imgCover.setPixmap(QPixmap(":/iconos/images/default_cover.png"))

    def edit_tag(self):
        self.titleEdit.setReadOnly(False)
        self.artistEdit.setReadOnly(False)
        self.albumEdit.setReadOnly(False)
        self.yearEdit.setReadOnly(False)
        self.trackEdit.setReadOnly(False)
        self.genreEdit.setReadOnly(False)
        self.composerEdit.setReadOnly(False)
        self.commentEdit.setReadOnly(False)

    def save_tag(self):
        audioFile = AudioFile()
        audioFile.title = self.titleEdit.text()
        self.titleEdit.setReadOnly(True)
        audioFile.album = self.albumEdit.text()
        self.albumEdit.setReadOnly(True)
        audioFile.artist = self.artistEdit.text()
        self.artistEdit.setReadOnly(True)
        audioFile.track_num = self.trackEdit.text()
        self.trackEdit.setReadOnly(True)
        audioFile.composer = self.composerEdit.text()
        self.composerEdit.setReadOnly(True)
        audioFile.year = self.yearEdit.text()
        self.yearEdit.setReadOnly(True)
        audioFile.genre = self.genreEdit.text()
        self.genreEdit.setReadOnly(True)
        audioFile.comment = self.commentEdit.toPlainText()
        self.commentEdit.setReadOnly(True)
        audio_path = self.mediaPlayer.get_path()
        self.tag.save_info(audioFile, audio_path)


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
