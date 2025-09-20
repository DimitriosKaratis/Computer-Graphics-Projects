import numpy as np
from t_shading_func import t_shading
from lookat_func import lookat
from world2view_func import world2view
from perspective_project_func import perspective_project
from rasterize_func import rasterize
from render_img_func import render_img

import matplotlib.pyplot as plt
from PIL import Image

def render_object(v_pos, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target, v_uvs, texImg):
    """
    Renders a textured 3D object from a specified camera viewpoint using a pinhole camera model.

    Parameters:
        v_pos (np.ndarray): Nx3 array of 3D vertex positions
        v_clr (np.ndarray): Nx3 array of RGB vertex colors (not used here, but included for compatibility)
        t_pos_idx (np.ndarray): Fx3 array of triangle indices
        plane_h (int): Height of the camera plane
        plane_w (int): Width of the camera plane
        res_h (int): Height of the output image (pixels)
        res_w (int): Width of the output image (pixels)
        focal (float): Focal length of the camera
        eye (np.ndarray): Camera position (3,)
        up (np.ndarray): Camera up vector (3,)
        target (np.ndarray): Point the camera is looking at (3,)
        v_uvs (np.ndarray): Nx2 array of UV coordinates for each vertex
        texImg (np.ndarray): Texture image to apply

    Returns:
        np.ndarray: res_h × res_w × 3 RGB image with the textured object rendered
    """
    # Step 1: Create blank white canvas
    image = np.ones((res_h, res_w, 3), dtype=np.float32)

    # Step 2: Compute view transformation (rotation and translation)
    R, t = lookat(eye, up, target)

    # Step 3: Transform to camera coordinates and perspective project them
    projected_pts, depth = perspective_project(v_pos.T, focal, R, t)


    # Step 4: Rasterize 2D points to image pixels
    pixel_coords = rasterize(projected_pts, plane_w, plane_h, res_w, res_h).T  # Nx2

    print("Depth stats:", depth.min(), depth.max())
    print("Pixel coords stats: x", pixel_coords[0].min(), pixel_coords[0].max(), "y", pixel_coords[1].min(), pixel_coords[1].max())



    # Step 5: Prepare vertex array for render_img (combine x, y with z-depth)
    # 'pixel_coords' is Nx2 (x, y), 'depth.T.flatten()' is Nx1 -> concat to Nx3
    vertices_2d = np.hstack([pixel_coords, depth.T.flatten()[:, None]])  # Nx3

    # Step 6: Render triangles using texture mapping
    image = render_img(t_pos_idx, vertices_2d, v_clr, v_uvs, depth.T.flatten(), texImg)

    return image


