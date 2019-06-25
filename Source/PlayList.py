import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Source.table_models import ListFile

AUDIO_PATH = os.path.expanduser('~')


class PlayList(QtWidgets.QMainWindow):
    def __init__(self, list_model, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.listModel = list_model

    def add_to_list_action(self):
        dialog_txt = "Choose mp3 file"
        options = "mp3 Files (*.mp3)"
        path = QFileDialog.getOpenFileName(self, dialog_txt, AUDIO_PATH, options)
        self.add_to_list(path)

    def add_to_list(self, path):
        if path[0].endswith('mp3'):
            list_file = ListFile(path[0])
            self.listModel.items.append(list_file)
            self.listModel.refresh()

    def remove_from_list(self):
        if self.tableView.selectedIndexes():
            index = self.tableView.selectedIndexes()[0]
            self.listModel.delete(index)

    def add_folder_to_list_action(self):
        dialog_txt = "Choose folder"
        folder = QFileDialog.getExistingDirectory(self, dialog_txt, AUDIO_PATH)
        self.add_folder_to_list(folder)

    def add_folder_to_list(self, folder):
        if folder:
            folder_list = os.listdir(folder)
            items = []
            for file in folder_list:
                if file.endswith('mp3'):
                    path = os.path.join(folder, file)
                    list_file = ListFile(path)
                    items.append(list_file)
                    items.sort(key=lambda x: x.name)
            self.listModel.items.extend(items)
            self.listModel.refresh()

    def get_path_from_list(self, index):
        path = self.listModel.get_path(index)
        return path
