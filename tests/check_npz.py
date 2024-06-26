import numpy as np
import sys

# Load the .npz file from input argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    print("Please provide the file path as an argument.")
    sys.exit(1)

data = np.load(file_path)

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