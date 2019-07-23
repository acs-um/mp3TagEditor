import eyed3
import io
from PyQt5 import QtWidgets
from datetime import datetime
from PIL import Image, ImageQt
from PyQt5.QtGui import QPixmap


class Tag(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

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

    def save_info(self):
        path = self.mediaPlayer.get_path()
        audio_file = eyed3.load(path)
        audio = audio_file.tag

        audio.title = self.titleEdit.text()
        self.titleEdit.setReadOnly(True)

        audio.album = self.albumEdit.text()
        self.albumEdit.setReadOnly(True)

        audio.artist = self.artistEdit.text()
        self.artistEdit.setReadOnly(True)

        audio.composer = self.composerEdit.text()
        self.composerEdit.setReadOnly(True)

        n_year = self.yearEdit.text()
        audio.recording_date = datetime(int(n_year), 1, 1)
        self.yearEdit.setReadOnly(True)

        var = self.trackEdit.text().strip(" ")
        var2 = var.split("/")
        var2[0] = int(var2[0])
        var2[1] = int(var2[1])
        list2 = tuple(var2)
        audio.track_num = list2
        self.trackEdit.setReadOnly(True)

        audio.genre = self.genreEdit.text()
        self.genreEdit.setReadOnly(True)

        # comment = self.commentEdit.toPlainText()
        # print(comment)
        # audio.comments = comment
        # self.commentEdit.setReadOnly(True)

        audio.save(self.mediaPlayer.get_path())
