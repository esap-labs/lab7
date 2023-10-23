import numpy as np
import torch

# Create a torch tensor
example_torch = torch.zeros((1, 1, 8, 8), dtype=torch.int32)

print("Tensor Shape: {}".format(np.shape(example_torch)))
print("Tensor before manipulation")
print(example_torch)

# Your code goes here


# End of your code

print("Tensor after manipulation")
print(example_torch)