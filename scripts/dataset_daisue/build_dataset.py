"""
Build Dataset Script

This script processes raw point cloud data by sampling points and creating normal vectors.
It loads a raw .npz file, scales the points, samples a specified number of points,
computes normals, and saves the processed data in both .npz and .ply formats.

Usage:
    python build_dataset.py [--num_points NUM_POINTS] [--scale_factor SCALE_FACTOR]

    --num_points: Number of points to sample (default: 400000)
    --scale_factor: Scale factor to apply to the points (default: 0.1)

After running this script, a new .npz file with the calculated normal vectors will be generated.
"""

import os
import argparse
from os.path import join, exists
import numpy as np
import trimesh
from src.utils.io import export_pointcloud

def create_dir(dir_in):
    """Create a directory if it doesn't exist."""
    if not exists(dir_in):
        os.makedirs(dir_in)

def load_input_npz(file_path):
    """Load input .npz file and return points."""
    data = np.load(file_path)
    points = data['points']
    return points

def scale_points(points, scale_factor):
    """Scale the points by a certain scale factor."""
    return points * scale_factor

def compute_normals(points):
    """Compute normals for a point cloud."""
    cloud = trimesh.points.PointCloud(points)
    hull = cloud.convex_hull
    sampled_points, face_idx = hull.sample(len(points), return_index=True)
    normals = hull.face_normals[face_idx]
    return normals

def sample_points(points, n_samples):
    """Sample the point cloud to a specified number of points."""
    if len(points) > n_samples:
        indices = np.random.choice(len(points), n_samples, replace=False)
        sampled_points = points[indices]
    else:
        indices = np.random.choice(len(points), n_samples, replace=True)
        sampled_points = points[indices]
    return sampled_points

def save_output_npz(file_path, points, normals):
    """Save points and normals to an output .npz file."""
    np.savez(file_path, points=points, normals=normals)

def main(num_points, scale_factor):
    # Constants and Paths
    OUT_PATH = 'data/daisue/processed'
    SCENE_NAME = 'area_0'
    OUTFILE = join(OUT_PATH, SCENE_NAME)
    INPUT_NPZ = 'data/daisue/raw/pointcloud.npz'  # Replace with actual input .npz file path

    create_dir(OUTFILE)

    # Parameters
    DTYPE = np.float16

    # Load input .npz file
    points = load_input_npz(INPUT_NPZ)

    # Scale points
    scaled_points = scale_points(points, scale_factor)

    # Sample points
    sampled_points = sample_points(scaled_points, num_points)

    # Compute normals
    normals = compute_normals(sampled_points)

    # Save surface points
    save_output_npz(join(OUTFILE, 'pointcloud.npz'), sampled_points.astype(DTYPE), normals.astype(DTYPE))
    export_pointcloud(sampled_points, join(OUTFILE, 'pointcloud.ply'))

    # Create test.lst file
    with open(join(OUT_PATH, 'test.lst'), "w") as file:
        file.write(SCENE_NAME)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process point cloud data.")
    parser.add_argument("--num_points", type=int, default=400000, help="Number of points to sample")
    parser.add_argument("--scale_factor", type=float, default=0.1, help="Scale factor to apply to the points")
    
    args = parser.parse_args()
    
    main(args.num_points, args.scale_factor)