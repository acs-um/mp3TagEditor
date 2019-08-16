import eyed3
from PyQt5 import QtWidgets
from datetime import datetime
from Source.AudioFile import AudioFile


class Tag(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

    def get_audio_info(self, path):
        audio_file = eyed3.load(path)
        return audio_file.tag

    def save_info(self, new_audio_file: AudioFile, audio_path):
        audio_file = eyed3.load(audio_path)
        old_audio = audio_file.tag

        old_audio.title = new_audio_file.title
        old_audio.album = new_audio_file.album
        old_audio.artist = new_audio_file.artist
        old_audio.composer = new_audio_file.composer

        n_year = new_audio_file.year
        old_audio.recording_date = datetime(int(n_year), 1, 1)
        var = new_audio_file.track_num.strip(" ")
        var2 = var.split("/")
        var2[0] = int(var2[0])
        var2[1] = int(var2[1])
        list2 = tuple(var2)
        old_audio.track_num = list2

        old_audio.genre = new_audio_file.genre

        # comment = new_audio_file.comment.toPlainText()
        # print(comment)
        # old_audio.comments = comment

        old_audio.save(audio_path)
