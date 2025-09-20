import numpy as np
from vector_interp import vector_interp

def t_shading(img, vertices, uv, textImg):
    """
    Applies texture mapping to a triangle using barycentric interpolation.

    :param img: The output image to be textured
    :param vertices: A (3 x 3) array of triangle vertex positions (x, y, z)
    :param uv: A (3 x 2) array of UV texture coordinates corresponding to each vertex
    :param textImg: The texture image (as a NumPy array)
    :return: Image with textured triangle
    """
    vertices = vertices.astype(float)
    uv = uv.astype(float)

    # Sort vertices by increasing y-coordinate for scanline rasterization
    sorted_indices = np.argsort(vertices[:, 1])
    C1, C2, C3 = vertices[sorted_indices]
    uv1, uv2, uv3 = uv[sorted_indices]

    # Determine the vertical range of scanlines (clamped to image bounds)
    y_min = int(max(0, np.floor(C1[1])))
    y_max = int(min(img.shape[0] - 1, np.ceil(C3[1])))

    # Loop over each scanline
    for y in range(y_min, y_max + 1):
        # Interpolate point A and its UV between C1 and C2 (top half) or C2 and C3 (bottom half)
        if y < C2[1]:
            A = vector_interp(C1, C2, C1, C2, y, 2)
            uv_A = vector_interp(C1, C2, uv1, uv2, y, 2)
        else:
            A = vector_interp(C2, C3, C2, C3, y, 2)
            uv_A = vector_interp(C2, C3, uv2, uv3, y, 2)

        # Interpolate point B and its UV between C1 and C3 
        B = vector_interp(C1, C3, C1, C3, y, 2)
        uv_B = vector_interp(C1, C3, uv1, uv3, y, 2)

        # Ensure A is to the left of B (for left-to-right horizontal interpolation)
        if A[0] > B[0]:
            A, B = B, A
            uv_A, uv_B = uv_B, uv_A

        # Determine horizontal range of pixels (clamped to image bounds)
        x_min = int(max(0, np.floor(A[0])))
        x_max = int(min(img.shape[1] - 1, np.ceil(B[0])))

        # Loop through each pixel on the scanline between A and B
        for x in range(x_min, x_max + 1):
            # Interpolate the UV coordinates at current pixel
            uv_P = vector_interp(A, B, uv_A, uv_B, x, 1)

            # Skip invalid UVs (outside [0, 1] or containing NaN)
            if np.any(np.isnan(uv_P)) or np.any(uv_P < 0) or np.any(uv_P > 1):
                continue

            # Map UV coordinates to texture pixel indices
            tex_x = int(np.clip(uv_P[0] * (textImg.shape[1] - 1), 0, textImg.shape[1] - 1))
            tex_y = int(np.clip(uv_P[1] * (textImg.shape[0] - 1), 0, textImg.shape[0] - 1))

            # Sample the texture and update the image
            img[y, x] = textImg[tex_y, tex_x]

    return img
