from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

numDataPerRank = 10
data = None
if (rank == 0):
    data = np.linspace(1, size*numDataPerRank, numDataPerRank*size)

recvbuf = np.empty(numDataPerRank, dtype='d')
comm.Scatter(data, recvbuf, root=0)

print('Rank: ',rank, ', recvbuf received: ', recvbuf)