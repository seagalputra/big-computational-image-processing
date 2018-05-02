import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io

def read_images(filename):
    """Function to read image from file
    
    Returns:
        image -- Variable that contains the N-Dimensional Matrix of image
    """

    image = io.imread(filename)
    return image

def show_images(image):
    """Method that show image from N-Dimensional Matrix
    
    Arguments:
        image {N-Dimensional Matrix} -- Variable that contains the N-Dimensional Matrix of image
    """

    plt.imshow(image)
    plt.show()
    