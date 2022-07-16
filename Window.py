from PyQt6.QtGui import QPainter, QPen, QBrush
from PyQt6.QtCore import Qt, QSize
from PyQt6 import QtCore, QtGui, QtWidgets, uic
import Raytracer as rt
from Sphere import Sphere
from Vec3 import Vec3

width = 640
height = 480
sphere = Sphere(Vec3(0, 1, -30), 5, Vec3(255, 0, 0))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("RayTracer")
        self.setMinimumSize(QSize(width, height))
        self.setGeometry(300, 300, 350, 300)
        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        rt.render(width, height, painter, sphere)
        painter.end()