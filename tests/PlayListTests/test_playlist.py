import pytest
import os
from app import MainWindows


def test_add_file(qtbot):
    widget = MainWindows()
    qtbot.addWidget(widget)
    path = [os.path.join(os.path.abspath("."), "tests/PlayListTests/25 - Bloodborne.mp3")]
    widget.playList.add_to_list(path)
    assert len(widget.listModel.items) == 1
    assert widget.listModel.items[0].name == "25 - Bloodborne.mp3"


def test_add_folder(qtbot):
    widget = MainWindows()
    qtbot.addWidget(widget)
    folder = os.path.join(os.path.abspath("."), "tests/PlayListTests")
    widget.playList.add_folder_to_list(folder)
    assert widget.listModel.rowCount() == 1
