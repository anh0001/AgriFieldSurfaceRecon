import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def calculate_bounding_box(points):
    min_bound = np.min(points, axis=0)
    max_bound = np.max(points, axis=0)
    return min_bound, max_bound

def visualize_bounding_box(ax, min_bound, max_bound):
    # Define the vertices of the bounding box
    vertices = [
        [min_bound[0], min_bound[1], min_bound[2]],
        [min_bound[0], min_bound[1], max_bound[2]],
        [min_bound[0], max_bound[1], min_bound[2]],
        [min_bound[0], max_bound[1], max_bound[2]],
        [max_bound[0], min_bound[1], min_bound[2]],
        [max_bound[0], min_bound[1], max_bound[2]],
        [max_bound[0], max_bound[1], min_bound[2]],
        [max_bound[0], max_bound[1], max_bound[2]],
    ]
    
    # Define the 12 edges composing the bounding box
    edges = [
        [vertices[0], vertices[1]], [vertices[0], vertices[2]], [vertices[0], vertices[4]],
        [vertices[1], vertices[3]], [vertices[1], vertices[5]], [vertices[2], vertices[3]],
        [vertices[2], vertices[6]], [vertices[3], vertices[7]], [vertices[4], vertices[5]],
        [vertices[4], vertices[6]], [vertices[5], vertices[7]], [vertices[6], vertices[7]],
    ]
    
    # Draw the bounding box
    for edge in edges:
        ax.plot3D(*zip(*edge), color="r")

def main():
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

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Access and inspect each array
    for key in keys:
        array = data[key]
        print(f"\nArray name: {key}")
        print(f"Shape: {array.shape}")
        print(f"Data type: {array.dtype}")
        print("Array contents:\n", array)
        
        # Check if the array contains 3D points
        if array.ndim == 2 and array.shape[1] == 3:
            min_bound, max_bound = calculate_bounding_box(array)
            print(f"Min bounding box for {key}: {min_bound}")
            print(f"Max bounding box for {key}: {max_bound}")
            print(f"x-axis: min {min_bound[0]}, max {max_bound[0]}")
            print(f"y-axis: min {min_bound[1]}, max {max_bound[1]}")
            print(f"z-axis: min {min_bound[2]}, max {max_bound[2]}")
            
            # Plot the points
            ax.scatter(array[:, 0], array[:, 1], array[:, 2], label=key)
            
            # Plot the bounding box
            visualize_bounding_box(ax, min_bound, max_bound)
        else:
            print(f"{key} is not a 3D points array.")

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    # Save the plot to a file
    plt.savefig('bounding_box_plot.png')
    print("Plot saved as bounding_box_plot.png")

if __name__ == "__main__":
    main()
