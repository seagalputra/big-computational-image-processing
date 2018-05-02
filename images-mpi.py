import numpy as np
import cv2
from mpi4py import MPI
import time
import matplotlib.pyplot as plt

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if (rank == 0):
    t1 = MPI.Wtime()
    img = cv2.imread('gambar.jpg', 0)
    t2 = MPI.Wtime()
    print('Time required to read the image is ', t2 - t1)
    # Find the image dimensions
    no_rows = int(img.shape[0])
    no_cols = int(img.shape[1])
    # Define local dimensions
    local_r = int(no_rows / size)
    local_c = int(no_cols / size)
    # Define image to be scattered to each node
    local_x = np.empty((no_rows, local_c), dtype='uint8')
    Inarray = np.array([no_rows, local_c])
else:
    # Define default 'None' Values for variables
    newimg = None
    no_rows = None
    img = None
    local_c = None
    Inarray = None

# Do the rest of the code in every node
t4 = MPI.Wtime()
Inarray = comm.bcast(Inarray, root=0)
no_rows = Inarray[0]
local_c = Inarray[1]
# Define local image on every node
local_x = np.empty((no_rows, local_c), dtype='uint8')
# Scatter the image in every node
comm.Scatterv(img, local_x, root=0)
# Define the local and total star count variables
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
comm.Reduce(local_star_count, total_star_count, op=MPI.SUM, root=0)

if (rank == 0):
    t5 = MPI.Wtime()
    # Print the time required to run the code
    print('Time required to complete the code is: ', t5 - t4)
    # Print the total number of stars
    print('Total star count is: ', total_star_count)
    # plt.imshow(img)
    # plt.show()
