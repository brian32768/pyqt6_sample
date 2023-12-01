import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

mylist = [
    '1',
    '2',
    '3'
]

mymap = {
    "name": "e911",
    "layers": [
        {
            "name": "Points of interest",
            "source": "database"
        },
        {
            "name": "Communication sites",
            "source": "database"
        }
    ]
}


class MainWindow(QtWidgets.QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFileSystemModel.html
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.currentPath())
        self.ui.treeView.setModel(model)

        self.ui.pushButton.clicked.connect(self.buttonClicked)

        #self.ui.show()

    def buttonClicked(self):

        for item in mylist:
            self.ui.listWidget.addItem(item)
                
        print("Click!")


if __name__ == "__main__":

    loader = QUiLoader()
    app = QtWidgets.QApplication([])
    ui = loader.load("myfirstui.ui", None)
    main = MainWindow(ui)
    main.show()
    sys.exit(app.exec())
