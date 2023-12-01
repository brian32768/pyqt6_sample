import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMessageBox
class thingie(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):

        self.setGeometry(100,100, 340,200)
        self.setWindowTitle("Plain old PyQT test")

        btn = QPushButton("Select APRX file", self)
        btn.move(10,10)
        btn.clicked.connect(self.dialog)

        self.show()

    def dialog(self):
        fname = QFileDialog.getOpenFileName(self,
            "Open project file", 
            '.',
            "Project files (*.aprx)")
        msg = QMessageBox.information(self, 
            "Processing", "Opening project " + fname[0],
            QMessageBox.StandardButton.Ok)
        msg.exec()

    def loggedin(self):
        msg = QMessageBox.information(self, 
                "Logged in", "You are now <b>logged in</b> and I feel good.",
                QMessageBox.StandardButton.Ok)
        msg.exec()


if __name__ == "__main__":

    app = QApplication([])
    window = thingie()
    sys.exit(app.exec())

