import numpy as np

# Load the .npz file
data = np.load('data/demo/Matterport3D_processed/17DRP5sb8fy/pointcloud.npz')

# List all keys in the .npz file
keys = list(data.keys())
print("Keys in the .npz file:", keys)

# Access and inspect each array
for key in keys:
    array = data[key]
    print(f"\nArray name: {key}")
    print(f"Shape: {array.shape}")
    print(f"Data type: {array.dtype}")
    print("Array contents:\n", array)