import sys
from PyQt6.QtWidgets import (QApplication, QWidget)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from myfirstui import Ui_MainWindow

mylist = [
    '1',
    '2',
    '3'
]

mymap = [
    "name": "e911",
    "layer": {
        "name": "Points of interest",
        "source": "database"
    },
    "layer": {
        "name": "Communication sites",
        "source": "database"
    },
]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.buttonClicked)

        self.show()

    def buttonClicked(self):
        for item in mylist:
            self.ui.listWidget.addItem(item)
        for item in mylist:
            self.ui.treeView.addItem(item)
        print("Click!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())