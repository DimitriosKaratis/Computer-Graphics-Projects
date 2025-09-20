import numpy as np
from f_shading import f_shading
from t_shading import t_shading

def render_img(faces, vertices, vcolors, uvs, depth, shading, texImg):
    """
    Renders a 3D scene by applying shading to triangles in the image.

    :param faces: A (n x 3) array where each row contains the indices of the vertices 
                  that form a triangle
    :param vertices: A (m x 3) array of 3D vertex positions (x, y, z)
    :param vcolors: A (m x 3) array of vertex colors (RGB) corresponding to each vertex
    :param uvs: A (m x 2) array of UV texture coordinates for each vertex
    :param depth: A (m,) array of depth values for each vertex
    :param shading: A string indicating the shading method ('f' for flat shading, 't' for texture shading)
    :param texImg: The texture image (as a NumPy array) to apply if texture shading is used
    :return: The rendered image with applied shading
    """
    M, N = 512, 512  # Canvas dimensions
    img = np.ones((M, N, 3))  # Create a white canvas

    # Calculate the depth of each triangle by averaging the depths of its vertices
    triangle_depths = np.mean(depth.flatten()[faces], axis=1)

    # Sort triangles by depth in descending order (farther triangles are rendered first)
    sorted_indices = np.argsort(-triangle_depths)
    faces_sorted = faces[sorted_indices]

    # Iterate through the sorted triangles to render them
    for i in range(faces_sorted.shape[0]):
        triangle_indices = faces_sorted[i].flatten()  # Get the vertex indices for the current triangle
        verts_2d = vertices[triangle_indices]     # 2D coordinates of the triangle's vertices
        colors = vcolors[triangle_indices]        # Vertex colors for the triangle
        uv_coords = uvs[triangle_indices]         # UV coordinates for the triangle's vertices

        # Print the details of the triangle being rendered
        print(f"Rendering triangle {i} with indices: {triangle_indices}")
        print(f"verts: {verts_2d}")

        # Apply shading based on the selected method ('f' for flat, 't' for texture)
        if shading == 'f':
            img = f_shading(img, verts_2d, colors)  
        elif shading == 't':
            img = t_shading(img, verts_2d, uv_coords, texImg)  
        else:
            raise ValueError("Shading must be either 'f' or 't'")  

    print("Total triangles rendered:", faces_sorted.shape[0])  # Print the number of triangles rendered
    print("Faces shape:", faces.shape)  # Print the shape of the faces array

    return img  # Return the final rendered image
