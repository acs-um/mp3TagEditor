import vlc
from PyQt5 import QtWidgets
import os


class MediaPlayer(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.is_paused = False
        self.is_play = False
        self.media = None
        self.path = None

    def play_pause(self):
        if self.is_playing():
            self.mediaplayer.pause()
            self.is_paused = True
            self.is_play = False
        else:
            if self.mediaplayer.play() == -1:
                self.media = self.instance.media_new(self.path)
                self.mediaplayer.set_media(self.media)
                self.mediaplayer.play()
            self.is_paused = False
            self.is_play = True

    def pause(self):
        if not self.is_playing():
            return
        self.mediaplayer.pause()
        self.is_paused = True
        self.is_play = False

    def play(self):
        if self.mediaplayer.play() == -1:
            self.media = self.instance.media_new(self.path)
            self.mediaplayer.set_media(self.media)
            self.mediaplayer.play()
        self.is_paused = False
        self.is_play = True

    def stop(self):
        self.mediaplayer.stop()

    def set_volume(self, volume):
        self.mediaplayer.audio_set_volume(volume)

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def is_playing(self):
        return self.is_play

    def open_file(self, path):
        if not path:
            dialog_txt = "Elija el archivo a reproducir"
            path = QtWidgets.QFileDialog.getOpenFileName(self, dialog_txt, os.path.expanduser('~/mp3TagEditor'))[0]

        if not path:
            return

        self.media = self.instance.media_new(path)

        self.mediaplayer.set_media(self.media)
        self.media.parse()

        self.play_pause()
