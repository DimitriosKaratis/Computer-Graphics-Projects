import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from t_shading import t_shading

# Path to save the output image
path_to_save = "test_t.png"

# Create a blank 400x400 black image (RGB)
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Define the 2D triangle vertices (x, y)
vertices = np.array([
    [100, 100],  # Vertex 1
    [300, 150],  # Vertex 2
    [200, 350]   # Vertex 3
])

# Define UV coordinates (u, v ∈ [0,1]) for each vertex
uv = np.array([
    [0.25, 0.25],  # Red (top-left)
    [0.75, 0.25],  # Green (top-right)
    [0.5, 0.75]    # Blue/Yellow (bottom)
])

# Load texture image from file (1200x1200 image)
textImg = mpimg.imread('texImg.jpg')

# Call the t_shading function to render the textured triangle
result_img = t_shading(img, vertices, uv, textImg)

# Display results side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)

# Create a copy of the texture image to draw the UV triangle
textImg_copy = textImg.copy()

# Convert UV coordinates to pixel coordinates on the texture image
h_tex, w_tex = textImg.shape[0], textImg.shape[1]
uv_pixels = (uv * np.array([w_tex - 1, h_tex - 1])).astype(int)

# Draw the triangle edges on the texture image
cv2.line(textImg_copy, tuple(uv_pixels[0]), tuple(uv_pixels[1]), (255, 255, 255), 2)
cv2.line(textImg_copy, tuple(uv_pixels[1]), tuple(uv_pixels[2]), (255, 255, 255), 2)
cv2.line(textImg_copy, tuple(uv_pixels[2]), tuple(uv_pixels[0]), (255, 255, 255), 2)

# Show the texture image with highlighted UV triangle
plt.imshow(textImg_copy)
plt.title('Texture Image')

# Show the result of the shaded triangle
plt.subplot(1, 2, 2)
plt.imshow(result_img)
plt.title('Shaded Triangle')

# Adjust layout and save the result
plt.tight_layout()
plt.savefig(path_to_save)
print("\nNew plot created")
plt.show()
