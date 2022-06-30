import numpy as np
import pandas as pd
from Vec3 import Vec3


class Matrix44:
    def __init__(self, m=np.identity(4)):
        self._m = m

    @classmethod
    def init_with_values(cls,
                         a, b, c, d,
                         e, f, g, h,
                         i, j, k, l,
                         m, n, o, p,
                         ):
        cls._m = np.identity(4)
        cls._m[0] = [a, b, c, d]
        cls._m[1] = [e, f, g, h]
        cls._m[2] = [i, j, k, l]
        cls._m[3] = [m, n, o, p]
        return Matrix44(cls._m)

    @classmethod
    def init_with_matrix(cls, m):
        cls._m = m
        return Matrix44(cls._m)

    def __str__(self):
        df = pd.DataFrame(self._m)
        return df.to_string(header=False, index=False)

    def __getitem__(self, item):
        return self._m[item]

    def __setitem__(self, key, value):
        self._m[key] = value

    def __mul__(self, other):
        if isinstance(other, Matrix44):
            return Matrix44(self._m * other._m)
        else:
            return Matrix44(self._m * other)

    def __add__(self, other):
        return Matrix44(self._m + other._m)

    def __sub__(self, other):
        return Matrix44(self._m - other._m)

    def __truediv__(self, other):
        return Matrix44(self._m / other._m)

    @staticmethod
    def mul_vec_matrix(v, m):
        x = v.x * m[0][0] + v.y * m[1][0] + v.z * m[2][0] + m[3][0]
        y = v.x * m[0][1] + v.y * m[1][1] + v.z * m[2][1] + m[3][1]
        z = v.x * m[0][2] + v.y * m[1][2] + v.z * m[2][2] + m[3][2]
        w = v.x * m[0][3] + v.y * m[1][3] + v.z * m[2][3] + m[3][3]
        if w != 1 and w != 0:
            x = x / w
            y = y / w
            z = z / w
        return Vec3(x, y, z)

    @staticmethod
    def mul_dir_matrix(v, m):
        x = v.x * m[0][0] + v.y * m[1][0] + v.z * m[2][0]
        y = v.x * m[0][1] + v.y * m[1][1] + v.z * m[2][1]
        z = v.x * m[0][2] + v.y * m[1][2] + v.z * m[2][2]
        return Vec3(x, y, z)

    def transpose(self):
        m = Matrix44()
        for i in range(4):
            for j in range(4):
                m[i][j] = self[j][i]
        self._m = m
        return m

    def invert(self):
        return Matrix44.init_with_matrix(np.linalg.inv(self._m))
