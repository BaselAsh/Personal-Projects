import sys
from PySide6.QtWidgets import *

class Buttons(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Two Buttons")
        button = QPushButton("First Button")
        button2 = QPushButton("Seconed Button")
        button3 = QPushButton("Third Button")
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button)
        buttons_layout.addWidget(button2)
        buttons_layout.addWidget(button3)
        button.clicked.connect(lambda: print("Button One Clicked"))
        button2.clicked.connect(lambda: print("Button Two Clicked"))
        self.setLayout(buttons_layout)



def main():
    app = QApplication(sys.argv)
    window = Buttons()
    window.setGeometry(100, 100, 1200, 500)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()