import pytest
from PyQt5 import QtCore
import os
from app import MainWindows


def test_play_file(qtbot):
    widget = MainWindows()
    qtbot.addWidget(widget)
    widget.mediaPlayer.set_path(os.path.join(os.path.abspath("."), "deamons.mp3"))
    assert widget.mediaPlayer.is_paused is False
    qtbot.mouseClick(widget.btnPlay, QtCore.Qt.LeftButton)
    print("First Click:", widget.mediaPlayer.is_playing())
    print("Path:", widget.mediaPlayer.get_path())
    assert widget.mediaPlayer.is_paused is False
    qtbot.mouseClick(widget.btnPlay, QtCore.Qt.LeftButton)
    print("Second Click:", widget.mediaPlayer.is_playing())
    assert widget.mediaPlayer.is_paused is True
