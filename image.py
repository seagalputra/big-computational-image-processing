import numpy as np
import matplotlib.pyplot as plt
import scipy
import skimage as sk
from skimage import io

def read_images(filename):
    """Function to read image from file.
    
    Returns:
        image -- Variable that contains the N-Dimensional Matrix of image.
    """

    image = io.imread(filename)
    return image

def show_images(image, color=None):
    """Show image using matplotlib.imshow function.
    
    Arguments:
        image {N-Dimensional Array} -- Variable that contains the N-Dimensional Matrix of image
        color {string} -- Color specify of the image
    """

    plt.imshow(image, cmap=color)
    plt.show()

def im2gray(image):
    """Convert RGB image into Grayscale image.
    
    Arguments:
        image {N-Dimensional Matrix} -- Variable that contains the N-Dimensional Matrix of image.
    
    Returns:
        N-Dimensional Matrix -- Return new image in grayscale color.
    
    To do :
        - Make this function run parallel
    """

    gray = sk.color.rgb2gray(image)
    return gray

def imrotate(image, angle):
    """Rotate image in specify angle
    
    Arguments:
        image {N-Dimensional Matrix} -- Variable that contains the N-Dimensional Matrix of image.
        angle {integer} -- Rotation angle value in degrees
    
    Returns:
        N-Dimensional Matrix -- Return new image in specified rotation

    To do:
        - Make this function run parallel
    """

    rotate = sk.transform.rotate(image, angle)
    return rotate

def imblur(image, s=None):
    """Image blur in specify sigma
    
    Arguments:
        image {N-Dimension Matrix} -- Variable that contains the N-Dimensional Matrix of image.
    
    Keyword Arguments:
        s {integer} -- Sigma value of blur kernel (default: {None})
    
    Returns:
        N-Dimensional Matrix -- Return new blured image
    """

    blur = scipy.ndimage.gaussian_filter(image, sigma=s)
    return blur