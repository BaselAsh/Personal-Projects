import os
import sys
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Button")
        button = QPushButton("First Press")
        self.setCentralWidget(button)
        self.count = 0
        button.clicked.connect(self.counter)

    def counter(self):
        """
        - Increament the count
        """
        self.count += 1
        print(self.count)


def main():
    """
    - The main function
    """
    start = datetime.datetime.now()
    app = QApplication(sys.argv)
    window = ButtonHolder()
    window.setGeometry(500, 300, 400, 200)
    window.show()
    app.exec()
    end = datetime.datetime.now()
    print(window.count)
    print(window.count / (end - start).seconds)


if __name__ == "__main__":
    main()
