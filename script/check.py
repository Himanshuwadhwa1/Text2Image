# Just to check if cuda is availabe and linked
import torch
print(torch.cuda.is_available())  # Should return True if CUDA is available
print(torch.cuda.current_device())  # Should return the GPU index if CUDA is available
print(torch.cuda.get_device_name(0))  # Prints the name of your GPU
