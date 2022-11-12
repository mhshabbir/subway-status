import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QMenuBar

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MTA Subway Status")
        self.resize(400,600)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()