import numpy as np
from Vec3 import Vec3


def spherical_to_cartesian(theta, phi):
    return Vec3(np.cos(phi) * np.sin(theta),
                np.sin(phi) * np.sin(theta),
                np.cos(theta))


def spherical_theta(v):
    return np.acos(np.clip(v.z, -1, 1))


def spherical_phi(v):
    phi = np.atan2(v.y, v.x)
    return phi + 2 * np.pi if phi < 0 else phi


def cos_theta(v):
    return v.z


def sin_theta_2(v):
    return np.max(0, 1 - cos_theta(v) ** 2)


def sin_theta(v):
    return np.sqrt(sin_theta_2(v))


def cos_phi(v):
    sintheta = sin_theta(v)
    if sintheta == 0:
        return 0
    return np.clip(v.y / sintheta, -1, 1)
