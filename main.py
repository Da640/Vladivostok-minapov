import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from UI import Ui_main

from random import randint


class Window(QWidget, Ui_main):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi(self)
        self.setGeometry(0, 0, 500, 500)
        self.draw_circle.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            pen = QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), 5)
            qp.setPen(pen)
            rad = randint(10, 100)
            qp.drawEllipse(randint(0, 400), randint(0, 300), rad, rad)
            pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.setPen(pen)
            rad = randint(10, 100)
            qp.drawEllipse(randint(0, 400), randint(0, 300), rad, rad)
            qp.end()
        self.do_paint = False

    def draw(self):
        self.do_paint = True
        self.update()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
