from Vec3 import Vec3
import numpy as np


class Sphere:
    def __init__(self,
                 center,
                 rad,
                 surf_col,
                 refl=0,
                 trans=0,
                 em_col=0,):
        self.center = center
        self.radius = rad
        self.radius2 = rad * rad
        self.surface_color = surf_col
        self.reflexion = refl
        self.transparency = trans
        self.emission_color = em_col

    def intersect(self,
                  ray_origin,
                  ray_dir,
                  t0,
                  t1,):
        l = self.center - ray_origin
        tca = l.dot(ray_dir)
        if tca < 0:
            print("false")
            return False
        d2 = l.dot(l) - tca * tca
        if d2 > self.radius2:
            return False
        thc = np.sqrt(self.radius2 - d2)
        t0 = tca - thc
        t1 = tca + thc
        return True

