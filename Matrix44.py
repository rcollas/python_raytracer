import re

import numpy as np
import pandas as pd


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
        m = Matrix44()
        for x in range(4):
            for y in range(4):
                m[x][y] = self._m[x][0] * other[0][y] + \
                          self._m[x][1] * other[1][y] + \
                          self._m[x][2] * other[2][y] + \
                          self._m[x][3] * other[3][y]
        return m
