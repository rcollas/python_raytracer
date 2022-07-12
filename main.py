import numpy as np
import matplotlib.pyplot as plt
from Vec3 import Vec3
from Sphere import Sphere
from Matrix44 import Matrix44

width = 640
inv_width = 1 / width
height = 480
inv_height = 1 / height
fov = 30
aspect_ratio = width / height
angle = np.tan(np.pi * 0.5 * fov / 180)
image = np.zeros((height, width, 3))
sphere = Sphere(Vec3(0, 1, -30), 5, Vec3(1, 0, 0))


def trace(ray_origin,
          ray_direction,
          spheres):
    if spheres.intersect(ray_origin, ray_direction, np.inf, np.inf):
        return (spheres.surface_color.x,
                spheres.surface_color.y,
                spheres.surface_color.z)
    return 1, 1, 1


def render():
    for y in range(height):
        for x in range(width):
            xx = (2 * ((x + 0.5) * inv_width) - 1) * angle * aspect_ratio
            yy = (1 - 2 * ((y + 0.5) * inv_height)) * angle
            ray_dir = Vec3(xx, yy, -1)
            ray_dir.normalize()
            image[y][x] = trace(Vec3(0, 0, 0), ray_dir, sphere)


render()



plt.imsave('image.png', image)
