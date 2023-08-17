"""
This file is for two vertical sliders next to each other horizontaly
This file was created in 18/7/2023 by Basel Ashraf 
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *


class SliderHolder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider")
        slider = QSlider(Qt.Orientation.Vertical, self)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider2 = QSlider(Qt.Orientation.Vertical, self)
        slider2.setMinimum(10)
        slider2.setMaximum(110)
        slider2.setValue(55)
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(slider)
        slider_layout.addWidget(slider2)
        self.setLayout(slider_layout)
        slider.valueChanged.connect(
            lambda value: print(f"Value 1 changed to : {value}")
        )
        slider2.valueChanged.connect(
            lambda value: print(f"Value 2 changed to : {value}")
        )


def main():
    app = QApplication(sys.argv)
    slider = SliderHolder()
    slider.setGeometry(50, 50, 1300, 700)
    slider.show()
    app.exec()


if __name__ == "__main__":
    main()
