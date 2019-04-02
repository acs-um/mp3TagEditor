from PyQt5.QtWidgets import QMainWindow, QApplication
from Source.mainWindows import Ui_MainWindow


class MainWindows(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):  # Constructor de la clase
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()
