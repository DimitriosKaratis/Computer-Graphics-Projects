import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

from render_object_func import render_object
from make_video_from_frames_func import make_video_from_frames


def generate_target_demo(demo_id, mode='forward' or 'target'):
    # Load data
    data = np.load("hw2.npy", allow_pickle=True).item()
    texImg = np.asarray(Image.open("stone-72_diffuse.jpg")) / 255.0

    # Object data
    v_pos = data['v_pos'].T
    v_uvs = data['v_uvs']
    t_pos_idx = np.array(data['t_pos_idx'])
    v_clr = np.ones_like(v_pos)

    # Scene parameters
    center = data['k_road_center']
    radius = data['k_road_radius']
    speed = data['car_velocity']
    cam_offset = data['k_cam_car_rel_pos']
    duration = data['k_duration']
    fps = data['k_fps']
    up = data['k_cam_up'].flatten()
    focal = data['k_f']
    plane_h = data['k_sensor_height']
    plane_w = data['k_sensor_width']
    res_h = res_w = 512
    k_cam_target = data['k_cam_target']


    # Output folder
    os.makedirs(f'demo_{demo_id}', exist_ok=True)

    total_frames = duration * fps
    omega = speed / radius  # angular velocity (rad/s)

    for frame in range(total_frames):
        t = frame / fps
        theta = omega * t

        # Car position on the circle
        car_pos = center + radius * np.array([np.cos(theta), 0, np.sin(theta)])

        # Velocity direction (tangent to the circle)
        tangent = np.array([-np.sin(theta), 0, np.cos(theta)])
        tangent /= np.linalg.norm(tangent)

        # Camera world position
        cam_pos = car_pos + cam_offset

        # Camera look direction is at specified target
        target = k_cam_target

        # Render frame
        img = render_object(
            v_pos=v_pos,
            v_clr=v_clr,
            t_pos_idx=t_pos_idx,
            plane_h=plane_h,
            plane_w=plane_w,
            res_h=res_h,
            res_w=res_w,
            focal=focal,
            eye=cam_pos,
            up=up,
            target=target,
            v_uvs=v_uvs,
            texImg=texImg
        )

        # Save frame
        plt.imsave(f'demo_{demo_id}/frame_{frame:03d}.png', img)
        print(f"Frame {frame}, cam_pos: {cam_pos}, target: {target}, tangent: {tangent}")



# Generate demo
generate_target_demo(demo_id='target', mode='target')

# Make video from the generated frames
make_video_from_frames("demo_target", "demo_target_video")