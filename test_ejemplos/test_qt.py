import pytest
from PyQt5 import QtCore
from time import sleep

from qt_example import Example


def test_button_text(qtbot):
    widget = Example()
    qtbot.addWidget(widget)

    assert widget.btn.text() == "Boton sin presionar"
    qtbot.mouseClick(widget.btn, QtCore.Qt.LeftButton)
    assert widget.btn.text() == "Boton #1"
    qtbot.mouseClick(widget.btn, QtCore.Qt.LeftButton)
    assert widget.btn.text() == "Boton #2"
    qtbot.mouseClick(widget.btn, QtCore.Qt.LeftButton)
