import os
import imageio.v2 as imageio

# Makes videos from the generated frames
def make_video_from_frames(folder, output_name, fps=25):
    frames = []
    for i in range(125):
        filename = os.path.join(folder, f"frame_{i:03d}.png")
        image = imageio.imread(filename)
        frames.append(image)

    output_path = f"{output_name}.mp4"
    imageio.mimsave(output_path, frames, fps=fps)
    print(f"Video saved as {output_path}")