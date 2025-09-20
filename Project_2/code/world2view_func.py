import numpy as np
from compose_func import compose

def world2view(pts: np.ndarray, R: np.ndarray, c0: np.ndarray) -> np.ndarray:
    """
    Transforms 3D points from world coordinates to camera view coordinates.
    
    Parameters:
        pts (np.ndarray): 3×N matrix of 3D points in world coordinates
        R (np.ndarray): 3×3 rotation matrix defining camera orientation
        c0 (np.ndarray): 3D vector defining camera position in world coordinates
    
    Returns:
        np.ndarray: N×3 matrix of transformed points in camera coordinates
    
    Transformation formula: view_coords = R @ (world_coords - c0)
    """
    # Ensure proper array shapes
    pts = np.asarray(pts)
    R = np.asarray(R)
    c0 = np.asarray(c0).reshape(3, 1)
    
    # Verify input shapes
    if pts.shape[0] != 3:
        pts = pts.T  # Transpose if N×3 was provided
        if pts.shape[0] != 3:
            raise ValueError("pts must be 3×N or N×3 array")
    if R.shape != (3, 3):
        raise ValueError("R must be 3×3 rotation matrix")
    if c0.shape != (3, 1):
        raise ValueError("c0 must be 3D vector")
    
    # Transform points: view = R*(world - c0)
    transformed = R @ (pts - c0)
    
    # Return as N×3 array
    return transformed.T


# # Example usage (comment or uncomment as needed)

# # World coordinates (3 points as 3×N matrix)
# pts = np.array([[1, 2, 3],  # X coords
#                 [4, 5, 6],  # Y coords 
#                 [7, 8, 9]]) # Z coords

# # Camera rotation (90° around Z-axis)
# R = np.array([[0, -1, 0],
#               [1, 0, 0],
#               [0, 0, 1]])

# # Camera position at (1,1,1)
# c0 = np.array([1, 1, 1])

# # Transform to view coordinates
# view_pts = world2view(pts, R, c0)
# print(view_pts)