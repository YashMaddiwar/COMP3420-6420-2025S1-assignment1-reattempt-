import numpy as np
import torch.nn as nn

# Task 1
def light_pixels(image, lightness, channel):
       """
       Given an image, return the number of pixels of the given channel whose intensity
       is higher than the number given in 'lightness'. Assume that the image is stored 
       as a numpy array with three channels for the colours 'red', 'green', and 'blue'.
       Also, assume that the intensity values are between 0 and 255.

       Parameters:
       image (numpy.ndarray): Input image array with shape (height, width, 3).
       lightness (int): The threshold value for the pixel intensity.
       channel (str): The channel name ('red', 'green', 'blue').

       Returns:
       int: The number of pixels with intensity higher than the given lightness

       Examples:
       >>> image = np.array([[[250,   2,   2], [  0,   2, 255], [  0,   0, 255]],
       ...                   [[  2,   2,  20], [250, 255, 255], [127, 127, 127]]])
       >>> light_pixels(image, 200, 'red')
       2
       >>> light_pixels(image, 200, 'green')
       1
       >>> light_pixels(image, 200, 'blue')
       3
       """
       # Determine how many pixels in the chosen colour channel are above a given threshold
       valid_channels = ["red", "green", "blue"]
       
       # Normalise input to lowercase and verify it is acceptable
       ch = channel.lower()
       if ch not in valid_channels:
              raise ValueError("Channel must be one of: 'red', 'green', or 'blue'.")
       
       # Figure out which slice of the array to use (0=R,1=G,2=B)
       idx = valid_channels.index(ch)
       
       # Build a boolean mask: True where pixel intensity exceeds the limit
       mask = image[:, :, idx] > lightness
       
       # Count all True values (i.e., qualifying pixels)
       count = int(mask.sum())
              
       return count

# Task 2
def decompose_image(image, thresholds):
       """
       Given a greyscale image and a list of intensity thresholds, return a list of masks.
       Each mask is a binary image where the pixel is 1 if the intensity of the
       corresponding pixel in the input image is higher than the threshold, and 0
       otherwise. Assume that the image is stored as a numpy array with two dimensions.
       Also, assume that the intensity values are between 0 and 255.

       Parameters:
       image (numpy.ndarray): Input image array with shape (height, width).
       thresholds (list of int): List of intensity thresholds.

       Returns:
       list of numpy.ndarray: List of binary masks.

       Examples:
       >>> image = np.array([[250, 120, 120], [0, 2, 255], [0, 0, 255]])
       >>> decompose_image(image, [200, 100])
       [array([[1, 0, 0],
              [0, 0, 1],
              [0, 0, 1]]), array([[1, 1, 1],
              [0, 0, 1],
              [0, 0, 1]])]
       """
       # Ensure the input is a 2D NumPy array (grayscale image).
       if not isinstance(image, np.ndarray) or image.ndim != 2:
              raise ValueError("Input must be a 2D numpy array (grayscale image).")
       
       # This will allow code to Convert thresholds into a list to allow multiple passes if needed.
       thresholds_list = list(thresholds)
       
       # Define a small helper function to create one mask for a single threshold.
       # For each pixel: if its value > threshold, mark it as 1; else mark it as 0.
       def make_mask(t):
              return np.where(image > t, 1, 0).astype(np.uint8)
       
       # We will now Use a list comprehension to build a binary mask for every threshold.
       masks = [make_mask(t) for t in thresholds_list]
       
       return masks

# Task 3
def build_deep_nn(input_size, layer_options, output_size):
       """Return a Torch neural model that has the following layers:
       - A sequence of hidden layers with ReLU activation functions; the 
         number of hidden layers is determined by the length of the 'layer_options' list.
         The size of hidden layer i is given by layer_options[i][0]. If layer_options[i][1] is
         a number larger than 0, then a dropout layer with that probability is added after 
         hidden layer i.
       - An output layer with size 'output_size'.
       The model must be generated using PyTorch's nn.Sequential class.

       Parameters:
       input_size (int): The size of the input layer.
       layer_options (list of tuples): A list of tuples where each tuple contains the size of 
                                        the hidden layer and the dropout probability.
       output_size (int): The size of the output layer.

       Returns:
       torch.nn.Sequential: The neural model.

       Examples:
       >>> model = build_deep_nn(10, [(20, 0), (30, 0.3)], 5)
       >>> model
       Sequential(
         (0): Linear(in_features=10, out_features=20, bias=True)
         (1): ReLU()
         (2): Linear(in_features=20, out_features=30, bias=True)
         (3): ReLU()
         (4): Dropout(p=0.3, inplace=False)
         (5): Linear(in_features=30, out_features=5, bias=True)
       )
       """
       return None       

if __name__ == "__main__":
     import doctest
     doctest.testmod()
