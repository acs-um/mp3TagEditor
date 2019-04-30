import vlc
from PyQt5 import QtWidgets
import os


class MediaPlayer(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.mediaplayer.audio_set_volume(70)
        self.is_paused = False
        self.media = None
        self.path = None

    def play_pause(self, path):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.is_paused = True
        else:
            if self.mediaplayer.play() == -1:
                self.open_file(path)
                return

            self.mediaplayer.play()
            self.is_paused = False

    def open_file(self, path):
        if not path:
            dialog_txt = "Elija el archivo a reproducir"
            path = QtWidgets.QFileDialog.getOpenFileName(self, dialog_txt, os.path.expanduser('~/mp3TagEditor'))[0]

        if not path:
            return

        self.media = self.instance.media_new(path)

        self.mediaplayer.set_media(self.media)
        self.media.parse()

        self.play_pause(path)
