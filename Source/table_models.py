from PyQt5.QtCore import QVariant, Qt, QAbstractTableModel


class ListFileModel(QAbstractTableModel):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items
        self.refresh()

    def refresh(self):
        self.layoutAboutToBeChanged.emit()
        self.layoutChanged.emit()
        self.modelReset.emit()

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.items)

    def columnCount(self, parent=None, *args, **kwargs):
        return 1

    def data(self, QModelIndex, role=None):
        if not QModelIndex.isValid():
            return QVariant()

        if role != Qt.DisplayRole:
            return QVariant()

        data = self.items[QModelIndex.row()].name
        return data

    def get_name(self, QModelIndex):
        return self.items[QModelIndex.row()].name

    def get_path(self, QModelIndex):
        return self.items[QModelIndex.row()].path

    def headerData(self, p_int, Qt_Orientation, role=None):
        return QVariant('Nombre')

    def delete(self, QModelIndex):
        self.items.pop(QModelIndex.row())
        self.refresh()


class ListFile:
    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1:][0]

    def __str__(self):
        return self.name
