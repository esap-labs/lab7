import torch
from torchvision import datasets, transforms
import cv2
import numpy as np

if __name__ == '__main__':

    # Load the MNIST dataset
    transform=transforms.Compose([ transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    testset = datasets.MNIST('lab7/data', train=False, download=True, transform=transform)
    test_loader = torch.utils.data.DataLoader(testset, batch_size=1, shuffle=False)

