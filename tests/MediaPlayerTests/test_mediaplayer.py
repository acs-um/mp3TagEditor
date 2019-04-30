import pytest
from PyQt5 import QtCore

from app import MainWindows


def test_play_file(qtbot):
    widget = MainWindows()
    qtbot.addWidget(widget)

    assert widget.mediaPlayer.is_paused is False
    qtbot.mouseClick(widget.btnPlay, QtCore.Qt.LeftButton)
    assert widget.mediaPlayer.is_paused is True
    qtbot.mouseClick(widget.btnPlay, QtCore.Qt.LeftButton)
    assert widget.mediaPlayer.is_paused is False
