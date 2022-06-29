import numpy as np
import pandas as pd
from Vec3 import Vec3


class Matrix44:
    def __init__(self):
        self._m = np.identity(4)

    def __str__(self):
        df = pd.DataFrame(self._m)
        return df.to_string(header=False, index=False)

    def __getitem__(self, item):
        return self._m[item]

    def __setitem__(self, key, value):
        self._m[key] = value

    def __mul__(self, other):
        return self._m * other._m

    def __add__(self, other):
        return self._m + other._m

    def __sub__(self, other):
        return self._m - other._m

    def __truediv__(self, other):
        return self._m / other._m

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

    @staticmethod
    def transpose(self):
        m = Matrix44()
        for i in range(4):
            for j in range(4):
                m[i][j] = self[j][i]
        return m
