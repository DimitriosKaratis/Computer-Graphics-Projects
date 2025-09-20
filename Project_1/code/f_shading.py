import numpy as np

def f_shading(img, vertices, vcolors):
    """
    Applies flat shading to a triangle in an image by filling it with the average color of its vertices.

    :param img: Input image as a NumPy array (H x W x 3)
    :param vertices: (3 x 3) array of triangle vertex positions (each row is x, y, z)
    :param vcolors: (3 x 3) array of RGB color values for each vertex
    :return: Updated image with the triangle shaded
    """
    # Make a copy of the image to avoid modifying the original
    updated_img = np.copy(img)

    # Extract only the x, y components of the triangle's vertices
    triangle = vertices[:, :2].copy()

    # Compute flat color as the average of the vertex colors
    flat_color = np.mean(vcolors, axis=0)

    # Determine bounding box of the triangle (to limit the rasterization area)
    min_x = max(int(np.floor(np.min(triangle[:, 0]))), 0)
    max_x = min(int(np.ceil(np.max(triangle[:, 0]))), img.shape[1] - 1)
    min_y = max(int(np.floor(np.min(triangle[:, 1]))), 0)
    max_y = min(int(np.ceil(np.max(triangle[:, 1]))), img.shape[0] - 1)

    # Generate a grid of pixel coordinates within the bounding box
    ys, xs = np.meshgrid(np.arange(min_y, max_y + 1), np.arange(min_x, max_x + 1), indexing='ij')
    points = np.stack([xs, ys], axis=-1).reshape(-1, 2)

    # Unpack triangle vertices
    A, B, C = triangle

    # Helper function to compute the cross product in 2D (used for point-in-triangle test)
    def cross(a, b, c):
        return (b[0]-a[0])*(c[:,1]-a[1]) - (b[1]-a[1])*(c[:,0]-a[0])

    # Compute the edge functions for all points
    d1 = cross(A, B, points)
    d2 = cross(B, C, points)
    d3 = cross(C, A, points)

    # Determine which points lie inside the triangle using sign consistency
    has_neg = (d1 < 0) | (d2 < 0) | (d3 < 0)
    has_pos = (d1 > 0) | (d2 > 0) | (d3 > 0)
    inside = ~(has_neg & has_pos)

    # Extract and loop through points inside the triangle to apply flat color
    inside_points = points[inside]
    for x, y in inside_points:
        updated_img[y, x] = flat_color

    return updated_img
