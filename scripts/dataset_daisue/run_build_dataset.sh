#!/bin/bash

# Set the PYTHONPATH environment variable
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run the Python script
python scripts/dataset_daisue/build_dataset.py
