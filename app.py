import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TMS")
        self.setFixedSize(QSize(1000, 700))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
