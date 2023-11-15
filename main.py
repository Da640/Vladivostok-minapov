import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw_circle.clicked.connect(self.draw_circle)

    def draw_circle(self):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(1, 40))
        qp.end()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
