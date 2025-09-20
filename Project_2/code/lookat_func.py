import numpy as np
from typing import Tuple

def lookat(eye: np.ndarray, up: np.ndarray, target: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes the camera's view transformation from eye position, up vector and target point.
    
    Parameters:
        eye (np.ndarray): 3D position of the camera center (shape: 3,)
        up (np.ndarray): Up vector of the camera (shape: 3,)
        target (np.ndarray): 3D target point the camera looks at (shape: 3,)
    
    Returns:
        Tuple[np.ndarray, np.ndarray]: 
            R (3×3): Rotation matrix from world to camera coordinates
            t (3,): Translation vector (camera position in world coordinates)
    
    The transformation follows: camera_coords = R @ (world_coords - t)
    """
    # Ensure inputs are numpy arrays and flatten them
    eye = np.asarray(eye).flatten()
    up = np.asarray(up).flatten()
    target = np.asarray(target).flatten()
    
    # Calculate camera's forward axis (z-axis in camera space)
    forward = target - eye
    forward = forward / np.linalg.norm(forward)
    
    # Calculate camera's right axis (x-axis in camera space)
    right = np.cross(forward, up)
    right = right / np.linalg.norm(right)
    
    # Recalculate the proper up axis (y-axis in camera space)
    up = np.cross(right, forward)
    up = up / np.linalg.norm(up)
    
    # Construct rotation matrix (world-to-camera)
    R = np.vstack([right, up, -forward]).T
    
    # Translation vector is the camera position
    t = eye
    
    return R, t


# # Example usage (comment or uncomment as needed)

# # Camera positioned at (2, 3, 5)
# eye = np.array([2, 3, 5])
# # Looking at origin
# target = np.array([0, 0, 0])
# # Up direction (world y-axis)
# up = np.array([0, 1, 0])

# R, t = lookat(eye, up, target)

# print("Rotation matrix R:")
# print(R)
# print("\nTranslation vector t:")
# print(t)

# ########################

# # World point
# p_world = np.array([0, 0, 0])  # target point

# # Transform to camera coordinates
# p_camera = R @ (p_world - t)

# print("Camera-space coordinates of target point:")
# print(p_camera)
