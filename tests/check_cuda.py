import torch
import torchvision

# Check if CUDA is available
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

# Print the CUDA version
if cuda_available:
    print(f"CUDA version: {torch.version.cuda}")

# Print the PyTorch and torchvision versions
print(f"PyTorch version: {torch.__version__}")
print(f"torchvision version: {torchvision.__version__}")

# Print the device name
if cuda_available:
    print(f"Device name: {torch.cuda.get_device_name(0)}")
