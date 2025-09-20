import numpy as np

def rasterize(pts_2d: np.ndarray, plane_w: int, plane_h: int, res_w: int, res_h: int) -> np.ndarray:
    """
    Converts 2D camera plane coordinates to pixel coordinates.
    
    Parameters:
        pts_2d (np.ndarray): 2×N matrix of 2D points in camera plane coordinates
        plane_w (int): Width of camera plane in world units
        plane_h (int): Height of camera plane in world units
        res_w (int): Width of output image in pixels
        res_h (int): Height of output image in pixels
    
    Returns:
        np.ndarray: 2×N matrix of integer pixel coordinates
    
    Coordinate Systems:
        - Camera plane: Origin at center, x right, y up
        - Image pixels: Origin at bottom-left, x right, y up
    """
    # Convert to numpy array if not already
    pts_2d = np.asarray(pts_2d)
    
    # Scale factors (pixels per world unit)
    scale_x = res_w / plane_w
    scale_y = res_h / plane_h
    
    # Center of image (pixel coordinates)
    center_x = res_w / 2
    center_y = res_h / 2
    
    # Convert to pixel coordinates
    pixel_x = pts_2d[0, :] * scale_x + center_x
    pixel_y = -pts_2d[1, :] * scale_y + center_y  # Flip y-axis
    
    # Round to nearest integer and clip to image bounds
    pixel_coords = np.vstack([
        np.clip(np.round(pixel_x), 0, res_w - 1),
        np.clip(np.round(pixel_y), 0, res_h - 1)
    ])
    
    return pixel_coords.astype(int)


# # Example usage (comment or uncomment as needed)

# # Sample 2D points in camera coordinates (2×N matrix)
# pts_2d = np.array([
#     [0.0, 0.5, -0.5],  # x coordinates
#     [0.0, 0.3, -0.2]   # y coordinates
# ])

# # Camera plane dimensions
# plane_w = 2.0  # meters
# plane_h = 1.5  # meters

# # Image resolution
# res_w = 640    # pixels
# res_h = 480    # pixels

# pixel_coords = rasterize(pts_2d, plane_w, plane_h, res_w, res_h)
# print(pixel_coords)