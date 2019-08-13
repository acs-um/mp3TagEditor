import pytest
from PyQt5 import QtCore
import os
from app import MainWindows


def test_play_file(qtbot):
    widget = MainWindows()
    qtbot.addWidget(widget)

    # Seteo el path con el archivo de audio
    # widget.mediaPlayer.set_path(os.path.join(os.path.abspath("."), "deamons.mp3"))
    widget.add_to_list([os.path.join(os.path.abspath("."), "deamons.mp3")])
    widget.tableView.selectRow(1)
    # Compruebo que la variable is_pause este en False
    assert widget.mediaPlayer.is_paused is False
    assert widget.mediaPlayer.is_play is False

    qtbot.mouseClick(widget.btnPlay, QtCore.Qt.LeftButton)
    assert widget.mediaPlayer.is_paused is False
    assert widget.mediaPlayer.is_play is True

    qtbot.mouseClick(widget.btnPlay, QtCore.Qt.LeftButton)
    assert widget.mediaPlayer.is_paused is True
    assert widget.mediaPlayer.is_play is False
