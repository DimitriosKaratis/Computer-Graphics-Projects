# Computer Graphics Projects

This repository contains the implementation of three projects in **Computer Graphics**, focusing on rasterization, transformations, projections, and shading.  
The work was developed as part of the *Computer Graphics course project* at the **Department of Electrical and Computer Engineering, Aristotle University of Thessaloniki**.

---

## 📌 Project 1 – Triangle Rasterization & Shading

The first project implements the core of rasterization: filling triangles on a 2D canvas and rendering 3D objects through projection.  

### Implemented Features
- **Linear interpolation function** (`vector_interp`)  
- **Flat shading** (`f_shading`):  
  - Triangles filled with the average color of their vertices.  
- **Texture mapping** (`t_shading`):  
  - Triangles shaded by interpolating texture coordinates and sampling a given texture image.  
- **Object rendering pipeline** (`render_img`):  
  - Combines faces, vertices, colors, texture coordinates, and depth sorting to render 3D objects onto a 2D canvas.  

### Demo Scripts
- `demo_f.py`: renders with **Flat shading**.  
- `demo_g.py`: renders with **Texture shading**.  

---

## 📌 Project 2 – Transformations & Projections

The second project extends the rasterization framework with geometric transformations, camera modeling, and perspective projection.

### Implemented Features
- **Affine transformations**:  
  - Translation (`translate`)  
  - Rotation (`rotate`)  
  - Composition of transformations (`compose`)  
- **Coordinate system transformation** (`world2view`)  
- **Camera orientation** (`lookat`)  
- **Pinhole perspective projection** (`perspective_project`)  
- **Rasterization to image coordinates** (`rasterize`)  
- **Full rendering pipeline** (`render_object`) using **Gouraud shading** (with texture mapping from Project 1).  

### Demo Scenarios
- **Car on circular road**: camera fixed, always looking forward.  
- **Car on circular road with target tracking**: camera rotates to look at a specified target point.  

Both demos generate image sequences simulating a 5-second animation at 25 FPS.

---

## 📌 Project 3 – Illumination & Shading Models

The third project introduces lighting models and advanced shading techniques to build a complete rendering pipeline.

### Implemented Features
- **Phong material class** (`MatPhong`) with parameters:
  - Ambient, diffuse, specular reflection coefficients, and Phong exponent.  
- **Lighting computation** (`light`):  
  - Handles multiple point light sources with ambient, diffuse, and specular contributions.  
- **Normal calculation** (`calc_normals`) per vertex of a triangle mesh.  
- **Rendering pipeline** (`render_object`):  
  - Supports **Gouraud shading** (`shade_gouraud`) and **Phong shading** (`shade_phong`).  

### Demo Script
- `demo.py`:  
  - Renders a 3D object from a given camera setup.  
  - Produces images under different lighting conditions:
    - Ambient only, diffuse only, specular only, and full lighting.  
  - Generates results for both **Gouraud** and **Phong shading**.  
  - Includes variations with individual light sources and combined lighting.  

---

## ⚙️ Technologies Used
- **Python 3.10**  
- **NumPy** – efficient vectorized operations.  
- **OpenCV / Matplotlib** – image handling and visualization.  
