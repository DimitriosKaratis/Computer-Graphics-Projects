import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from render_img import render_img

# Path where the rendered image will be saved
path_to_save = "render_f.png"  

# Load data from the .npy file
data = np.load('hw1.npy', allow_pickle=True).item()

# Read texture image
texImg = mpimg.imread('texImg.jpg')

# Normalize texture image to the range [0, 1] if it is of type uint8
if texImg.dtype == np.uint8:
    texImg = texImg / 255.0  

# Get the face indices from the loaded data
faces = data['t_pos_idx']

# Perform the flat shading 
img_texture = render_img(
    faces=data['t_pos_idx'],
    vertices=data['v_pos2d'],
    vcolors=data['v_clr'],
    uvs=data['v_uvs'],
    depth=data['depth'].reshape(-1, 1),
    shading='f', 
    texImg=texImg
)

# Display the rendered texture image
plt.figure(figsize=(12, 6))
plt.imshow(img_texture)
plt.title("F Shading")  
plt.axis('off')  

# Save the rendered image to the specified path and show it
plt.savefig(path_to_save)
print("\nNew plot created") 
plt.show() 
