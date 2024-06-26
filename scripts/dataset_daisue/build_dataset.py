import os
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

def compute_normals(points):
    """Compute normals for a point cloud."""
    # Create a Trimesh object from points
    cloud = trimesh.points.PointCloud(points)
    # Create a convex hull from the point cloud
    hull = cloud.convex_hull
    # Sample points from the hull to get normals
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

# Constants and Paths
OUT_PATH = 'data/daisue/processed'
SCENE_NAME = 'area_0'
OUTFILE = join(OUT_PATH, SCENE_NAME)
INPUT_NPZ = 'data/daisue/raw/pointcloud.npz'  # Replace with actual input .npz file path

create_dir(OUTFILE)

# Parameters
N_POINTCLOUD_POINTS = 400000
DTYPE = np.float16

# Load input .npz file
points = load_input_npz(INPUT_NPZ)

# Sample points
sampled_points = sample_points(points, N_POINTCLOUD_POINTS)

# Compute normals
normals = compute_normals(sampled_points)

# Save surface points
save_output_npz(join(OUTFILE, 'pointcloud.npz'), sampled_points.astype(DTYPE), normals.astype(DTYPE))
export_pointcloud(sampled_points, join(OUTFILE, 'pointcloud.ply'))

# Create test.lst file
with open(join(OUT_PATH, 'test.lst'), "w") as file:
    file.write(SCENE_NAME)
