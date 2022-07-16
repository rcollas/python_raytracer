import numpy as np
from Vec3 import Vec3
from PyQt6.QtCore import Qt
from PyQt6 import QtGui


def trace(ray_origin,
          ray_direction,
          spheres):
    if spheres.intersect(ray_origin, ray_direction, np.inf, np.inf):
        return spheres.surface_color.to_hex()
    return Qt.GlobalColor.white


def render(width, height, painter, objs):
    inv_width = 1 / width
    inv_height = 1 / height
    fov = 30
    aspect_ratio = width / height
    angle = np.tan(np.pi * 0.5 * fov / 180)

    for x in range(width):
        for y in range(height):
            xx = (2 * ((x + 0.5) * inv_width) - 1) * angle * aspect_ratio
            yy = (1 - 2 * ((y + 0.5) * inv_height)) * angle
            ray_dir = Vec3(xx, yy, -1)
            ray_dir.normalize()
            col = trace(Vec3(0, 0, 0), ray_dir, objs)
            painter.setPen(QtGui.QColor(col))
            painter.drawPoint(x, y)
