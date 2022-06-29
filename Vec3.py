import numpy as np


class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @staticmethod
    def normalize(v):
        return v / v.norm()

    @staticmethod
    def dot(a, b):
        return a.x * b.x + \
               a.y * b.y + \
               a.z * b.z

    @staticmethod
    def cross(a, b):
        x = a.y * b.z - a.z * b.y
        y = a.x * b.x - a.x * b.z
        z = a.z * b.y - a.y * b.x
        return Vec3(x, y, z)

    def __str__(self):
        return "x:{0}, y:{1}, z:{2}".format(self.x, self.y, self.z)

    def __truediv__(self, v):
        if isinstance(v, Vec3):
            return Vec3(self.x / v.x, self.y / v.y, self.z / v.z)
        return Vec3(self.x / v, self.y / v, self.z / v)

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
