import numpy as np
import cv2
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if (rank == 0):
    t1 = MPI.Wtime()
    img = cv2.imread('gambar.jpg', 0)
    t2 = MPI.Wtime()
    print('Time required to read the image is ', t2 - t1)
    # Find the image dimensions
    height = int(img.shape[0])
    width = int(img.shape[1])
    # Define local dimensions, break image into several parts
    local_h = int(height / size)
    local_w = int(width / size)
    # Define image to be scattered to each node
    local_x = np.empty((height, local_w), dtype='uint8')
    Inarray = np.array([height, local_w])
else:
    # Define default 'None' values for variables
    new_img = None
    height = None
    img = None
    local_w = None
    Inarray = None

# Do the rest of the code in every node
t4 = MPI.Wtime()
Inarray = comm.bcast(Inarray, root=0)
no_rows = Inarray[0]
local_w = Inarray[1]
# Define local image on every node
local_x = np.empty((no_rows, local_w), dtype='uint8')
# Scatter the image in every node
local_star_count = np.arange(1)
total_star_count = np.arange(1)
# Logic to count stars
img_node_thresh = cv2.adaptiveThreshold(
    local_x, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 59, 0)
# Logic to count stars in each node
local_star_count = ((200 < img_node_thresh)).sum()
# Print the value of star count in each node
print('Number of stars in Node', rank, 'is: ', local_star_count)
# Reduce the local counts into total star count variable using reduce function
