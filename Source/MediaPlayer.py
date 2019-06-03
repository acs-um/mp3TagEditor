import vlc
from PyQt5 import QtWidgets
import os


class MediaPlayer(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.is_paused = False
        self.media = None
        self.path = None

    def play_pause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.is_paused = True
            print("Pausado")
        else:
            if self.mediaplayer.play() == -1:
                self.media = self.instance.media_new(self.path)
                self.mediaplayer.set_media(self.media)
                # self.media.parse()
                self.mediaplayer.play()
                print("Reproduciendo")
            self.is_paused = False

    def stop(self):
        self.mediaplayer.stop()

    def set_volume(self, volume):
        self.mediaplayer.audio_set_volume(volume)

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def is_playing(self):
        return self.mediaplayer.is_playing()

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
