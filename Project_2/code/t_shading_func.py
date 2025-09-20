import numpy as np
from vector_interp_func import vector_interp

def t_shading(img, vertices, uv, textImg, colors):
    """
    Applies Gouraud shading and texture mapping to a triangle using barycentric interpolation.

    :param img: The output image to be textured (HxWx3)
    :param vertices: A (3 x 3) array of triangle vertex positions (x, y, z)
    :param uv: A (3 x 2) array of UV texture coordinates corresponding to each vertex
    :param textImg: The texture image (as a NumPy array)
    :param colors: A (3 x 3) array of RGB vertex colors
    :return: Image with shaded + textured triangle
    """
    vertices = vertices.astype(float)
    uv = uv.astype(float)
    colors = colors.astype(float)

    # Sort vertices by y-coordinate for scanline rasterization
    sorted_indices = np.argsort(vertices[:, 1])
    C1, C2, C3 = vertices[sorted_indices]
    uv1, uv2, uv3 = uv[sorted_indices]
    col1, col2, col3 = colors[sorted_indices]

    y_min = int(max(0, np.floor(C1[1])))
    y_max = int(min(img.shape[0] - 1, np.ceil(C3[1])))

    for y in range(y_min, y_max + 1):
        if y < C2[1]:
            A = vector_interp(C1, C2, C1, C2, y, 2)
            uv_A = vector_interp(C1, C2, uv1, uv2, y, 2)
            col_A = vector_interp(C1, C2, col1, col2, y, 2)
        else:
            A = vector_interp(C2, C3, C2, C3, y, 2)
            uv_A = vector_interp(C2, C3, uv2, uv3, y, 2)
            col_A = vector_interp(C2, C3, col2, col3, y, 2)

        B = vector_interp(C1, C3, C1, C3, y, 2)
        uv_B = vector_interp(C1, C3, uv1, uv3, y, 2)
        col_B = vector_interp(C1, C3, col1, col3, y, 2)

        if A[0] > B[0]:
            A, B = B, A
            uv_A, uv_B = uv_B, uv_A
            col_A, col_B = col_B, col_A

        x_min = int(max(0, np.floor(A[0])))
        x_max = int(min(img.shape[1] - 1, np.ceil(B[0])))

        for x in range(x_min, x_max + 1):
            uv_P = vector_interp(A, B, uv_A, uv_B, x, 1)
            col_P = vector_interp(A, B, col_A, col_B, x, 1)

            if np.any(np.isnan(uv_P)) or np.any(uv_P < 0) or np.any(uv_P > 1):
                continue

            tex_x = int(np.clip(uv_P[0] * (textImg.shape[1] - 1), 0, textImg.shape[1] - 1))
            tex_y = int(np.clip(uv_P[1] * (textImg.shape[0] - 1), 0, textImg.shape[0] - 1))

            tex_color = textImg[tex_y, tex_x]
            final_color = col_P * tex_color

            img[y, x] = final_color

    return img
