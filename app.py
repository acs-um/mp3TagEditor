import sys
import os
import eyed3
import io

from PyQt5.QtWidgets import QFileDialog, QHeaderView, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5 import QtWidgets
from Source.mainWindows import Ui_MainWindow
from Source.MediaPlayer import MediaPlayer
from Source.table_models import ListFileModel, ListFile
from PIL import Image, ImageQt

AUDIO_PATH = os.path.expanduser('~/Escritorio')


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # self.volume = 80
        # self.mediaPlayer = MediaPlayer()
        # self.mediaPlayer.set_volume(self.volume)
        # self.volumeSlider.setValue(self.volume)
        # self.volumeSlider.valueChanged.connect(self.mediaPlayer.set_volume)
        # self.btnPlay.clicked.connect(self.mediaPlayer.play_pause)
        # self.btnStop.clicked.connect(self.mediaPlayer.stop)
        self.itemsList = []
        self.listModel = ListFileModel(self.itemsList, parent=self)
        self.tableView.setModel(self.listModel)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.doubleClicked.connect(self.play_from_list)
        self.btnAddListMenu.triggered.connect(self.add_to_list_action)
        self.btnAddFolderListMenu.triggered.connect(self.add_folder_to_list)
        self.shortcut = QShortcut(QKeySequence("Delete"), self)
        self.shortcut.activated.connect(self.remove_from_list)
        self.btnSave.clicked.connect(self.save_info)
        self.path = None

    def set_path(self, file):
        self.path = file

    def add_to_list_action(self):
        dialog_txt = "Choose mp3 file"
        options = "mp3 Files (*.mp3)"
        path = QFileDialog.getOpenFileName(self, dialog_txt, AUDIO_PATH, options)
        self.add_to_list(path)

    def add_to_list(self, path):
        if path[0].endswith('mp3'):
            list_file = ListFile(path[0])
            self.listModel.items.append(list_file)
            self.listModel.refresh()

    def remove_from_list(self):
        if self.tableView.selectedIndexes():
            index = self.tableView.selectedIndexes()[0]
            self.listModel.delete(index)

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
                    items.sort(key=lambda x: x.name)
            self.listModel.items.extend(items)
            self.listModel.refresh()

    def play_from_list(self):
        index = self.tableView.selectedIndexes()[0]
        file = self.listModel.get_path(index)

        self.set_path(file)

        self.mediaPlayer.set_path(file)
        self.mediaPlayer.play_pause()
        self.load_info(file)
        self.btnEdit.clicked.connect(self.edit_tag)

    def load_info(self, file):
        audiofile = eyed3.load(file)
        audio = audiofile.tag

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

        format_track = "{}/{}".format(audio.track_num[0], audio.track_num[1])
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
        print(self.path)
        self.titleEdit.setReadOnly(False)
        self.artistEdit.setReadOnly(False)
        self.albumEdit.setReadOnly(False)
        self.yearEdit.setReadOnly(False)
        self.trackEdit.setReadOnly(False)
        self.genreEdit.setReadOnly(False)
        self.composerEdit.setReadOnly(False)
        self.commentEdit.setReadOnly(False)

    def save_info(self):
        print(self.titleEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec_())
