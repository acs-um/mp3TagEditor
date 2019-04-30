from PyQt5 import QtWidgets

from Source.MediaPlayer import MediaPlayer
from Source.mainWindows import Ui_MainWindow
import sys


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.mediaPlayer = MediaPlayer()
        self.btnPlay.clicked.connect(self.mediaPlayer.play_pause)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec_())
