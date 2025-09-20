import numpy as np
from math import cos, sin, sqrt

def rotate(axis, angle, center=np.zeros(3)):
    """
    Create a 4x4 homogeneous rotation matrix for rotating `angle` radians
    around the specified `axis`, optionally around a given `center`.

    Parameters:
        axis (np.ndarray): Rotation axis (3,)
        angle (float): Rotation angle in radians
        center (np.ndarray): Rotation center (3,), default is origin

    Returns:
        np.ndarray: 4x4 homogeneous rotation matrix
    """
    axis = axis / np.linalg.norm(axis)
    x, y, z = axis
    c = np.cos(angle)
    s = np.sin(angle)
    C = 1 - c

    # 3x3 rotation matrix using Rodrigues' formula
    R = np.array([
        [x*x*C + c,   x*y*C - z*s, x*z*C + y*s],
        [y*x*C + z*s, y*y*C + c,   y*z*C - x*s],
        [z*x*C - y*s, z*y*C + x*s, z*z*C + c  ]
    ])

    # Embed in 4x4 matrix
    xform = np.eye(4)
    xform[:3, :3] = R

    # Apply translation if center is not the origin
    if np.any(center != 0):
        T1 = np.eye(4)
        T2 = np.eye(4)
        T1[:3, 3] = -center
        T2[:3, 3] = center
        xform = T2 @ xform @ T1

    return xform

# # Example usage (comment or uncomment as needed)
# axis = np.array([0, 0, 1])         
# angle = np.pi / 2                   
# center = np.array([1, 0, 0])        
# xform = rotate(axis, angle, center)
# print(np.round(xform, 3))
