import sys
import os
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import *


class MenuBar(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.resize(500, 300)
        self.setWindowTitle("Menu Bar")
        self.app = app
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(lambda: sys.exit())

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("&Window")
        settings = menu_bar.addMenu("&Settings")
        dir = settings.addAction("Dir")
        dir.triggered.connect(lambda: print(os.system("dir")))
        menu_bar.addMenu("&Help")

        toolbar = QToolBar("This is my first toolbar")
        toolbar.setIconSize(QSize(16, 16))
        toolbar.addAction(quit_action)
        self.addToolBar(toolbar)

        action = QAction("First Action", self)
        action.setStatusTip("This is my status message")
        action.triggered.connect(lambda: print("This is QAction"))
        toolbar.addAction(action)

        


def main():
    app = QApplication(sys.argv)
    window = MenuBar(app)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()