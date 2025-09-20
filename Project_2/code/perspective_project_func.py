import numpy as np
from typing import Tuple
from world2view_func import world2view

def perspective_project(pts: np.ndarray, focal: float, 
                        R: np.ndarray, t: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Projects 3D points to 2D image plane using pinhole camera model.
    
    Parameters:
        pts (np.ndarray): 3×N matrix of 3D points in world coordinates
        focal (float): Focal length (distance from camera center to image plane)
        R (np.ndarray): 3×3 rotation matrix (world-to-camera)
        t (np.ndarray): 3D translation vector (camera position)
    
    Returns:
        Tuple[np.ndarray, np.ndarray]: (2×N image coordinates, 1×N depths)
    """

    # Ensure shapes
    pts = np.asarray(pts)
    if pts.shape[0] != 3:
        pts = pts.T
    t = t.reshape(3, 1)

    # Transform to camera coordinates
    camera_pts = world2view(pts, R, t).T
    depths = camera_pts[2, :]

    # Perspective projection
    projected_pts = focal * camera_pts[:2, :] / depths

    return projected_pts, depths


# # Example usage (comment or uncomment as needed)

# # Sample 3D points (3×N matrix)
# pts = np.array([[1, 2, 3],   # X coordinates
#                 [4, 5, 6],   # Y coordinates
#                 [7, 8, 9]])  # Z coordinates

# # Camera parameters
# focal = 1.0
# R = np.eye(3)  # Identity rotation (camera aligned with world axes)
# t = np.array([0, 0, 0])  # Camera at origin

# projected, depths = perspective_project(pts, focal, R, t)

# print("Projected points:")
# print(projected)
# print("\nDepths:")
# print(depths)