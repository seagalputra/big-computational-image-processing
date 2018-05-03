import numpy as np
import image
import matplotlib.pyplot as plt
import multiprocessing
import skimage
from skimage import io

img = io.imread('gambar.jpg')

p1 = multiprocessing.Process(target = image.im2gray, args = (img,))
p2 = multiprocessing.Process(target = image.imrotate, args = (img, 90))

p1.start()
p2.start()

p1.join()
p2.join()