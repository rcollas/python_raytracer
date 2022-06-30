import numpy as np
import matplotlib.pyplot as plt
from Vec3 import Vec3
from Matrix44 import Matrix44

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
print(Vec3(200, 0, 1) + Vec3(0, -23, 100))

matrix = Matrix44()

print(matrix)
print(matrix[0])
print(matrix[0][0])
matrix += Matrix44()
matrix *= 3
print(matrix)
matrix[0] = [-1, 2, 0.324, 10]
print(Matrix44.mul_vec_matrix(Vec3(10, 4, -10), matrix))
print(matrix)
print(matrix.transpose())
print(Vec3())
print(Matrix44())
init_matrix = Matrix44.init_with_values(0.707107, 0, -0.707107, 0,
                                        -0.331295, 0.883452, -0.331295, 0,
                                        0.624695, 0.468521, 0.624695, 0,
                                        4.000574, 3.00043, 4.000574, 1)
#print(Matrix44().invert())
print(init_matrix)
print("\n")
print("init_matrix.invert()")
print(init_matrix.invert())

# for x in range(width):
#     for y in range(height):
#         color = np.zeros(3)
#         color = (0.5 * (x / height), 0.2 * (x / height), 0.7)
#         image[x, y] = np.clip(color, 0, 1)

plt.imsave('image.png', image)
