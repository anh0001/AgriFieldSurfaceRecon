
# Surface Reconstruction in Agriculture

This project aims to reconstruct surfaces from point clouds, generate a mesh, and visualize it using 3D viewers such as MeshLab.

## Installation

### Step 1: Create an Anaconda Environment

First, create an Anaconda environment called `conv_onet` using the provided `environment.yaml` file.

```bash
conda env create -f environment.yaml
conda activate conv_onet
```

### Step 2: Compile the Extension Modules

Next, compile the extension modules required for the project.

```bash
python setup.py build_ext --inplace
```

## Data Preparation

### Step 3: Prepare Your Data

1. Place your raw data in the `data/raw` folder.
2. Place your `.npz` data into the `data` folder, such as `data/daisue/raw` folder. The `.npz` file should contain a `points` variable storing each point in an `(x, y, z)` format.

### Step 4: Build the Data

To process your raw data by sampling and creating normal vectors, run the following bash script:

```bash
bash scripts/dataset_daisue/run_build_dataset.sh
```

After running the script, a new `.npz` file with the normals vector calculated will be generated. You can check the code in `scripts/dataset_daisue/build_dataset.py` for more details.

## Running the Surface Reconstruction

To reconstruct the surface using a pretrained model trained on Matterport3D, run the following command:

```bash
python generate.py configs/pointcloud_crop/daisue.yaml
```

## Viewing the Mesh

After generating the mesh, you can view it using 3D viewers such as [MeshLab](https://www.meshlab.net/).

## References

This project is modified from [Convolutional Occupancy Networks](https://github.com/autonomousvision/convolutional_occupancy_networks).

## License

This project is licensed under the terms of the MIT license.
