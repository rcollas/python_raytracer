import numpy as np
import matplotlib.pyplot as plt
from Vec3 import Vec3

width = 300
height = 300


image = np.zeros((height, width, 3))

vector = Vec3(10, 255, 0)
print(vector.norm())
print(vector)
vector = Vec3.normalize(vector)
print(vector)
print(vector.norm())
print(Vec3.dot(vector, Vec3(200, 0, 45)))

# for x in range(width):
#     for y in range(height):
#         color = np.zeros(3)
#         color = (0.5 * (x / height), 0.2 * (x / height), 0.7)
#         image[x, y] = np.clip(color, 0, 1)

plt.imsave('image.png', image)
