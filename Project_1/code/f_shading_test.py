import numpy as np
import matplotlib.pyplot as plt
from f_shading import f_shading

# Path to save the output image
path_to_save = "test_f.png"

# Create a 100x100 white image
img = np.ones((100, 100, 3)) 

# Define the vertices of the triangle (x, y)
vertices = np.array([[20, 20], [80, 20], [50, 80]])  

# Define the vertex colors (RGB), Red, Green, Blue
vcolors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  

# Apply the f_shading function to shade the triangle
updated = f_shading(img, vertices, vcolors)

# Create a figure with 1 row and 2 columns for displaying the results
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot the triangle outline and colored vertices on the LEFT
axs[0].imshow(img)  
axs[0].set_title('Triangle Outline & Vertices')  
axs[0].axis('off') 

# Draw the triangle outline by connecting the vertices
triangle = np.vstack([vertices, vertices[0]])  
axs[0].plot(triangle[:, 0], triangle[:, 1], color='black')  # Draw the triangle outline in black

# Plot the vertices with their respective colors
for (x, y), color in zip(vertices, vcolors):
    axs[0].scatter(x, y, color=color, s=100, edgecolors='black')  

# Plot the shaded triangle on the RIGHT
axs[1].imshow(updated)  
axs[1].set_title('Shaded Triangle')  
axs[1].axis('off')  

# Save and show the final plot
plt.tight_layout()  
plt.savefig(path_to_save)  
print("\nNew plot created")  
plt.show()  
