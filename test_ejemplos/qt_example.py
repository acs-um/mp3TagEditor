#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.contador = 0
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.btn = QPushButton('Boton sin presionar', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.cambiar_text)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Ejemplo')
        self.show()

    def cambiar_text(self):
        sender = self.sender()
        self.contador += 1
        sender.setText(f"Boton #{self.contador}")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
