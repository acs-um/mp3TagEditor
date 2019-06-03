import pytest
from app import MainWindows


def test_add_file(qtbot):
    widget = MainWindows()
    qtbot.addWidget(widget)
    path = ["./tests/PlayListTests/25 - Bloodborne.mp3"]
    widget.add_to_list(path)
    assert len(widget.listModel.items) == 1
    assert widget.listModel.items[0].name == "25 - Bloodborne.mp3"
