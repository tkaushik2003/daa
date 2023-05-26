from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    a = 1000
    numbers = np.random.rand(a)
else:
    numbers = None

local_n = a // size
local_numbers = np.zeros(local_n)

comm.Scatter(numbers, local_numbers, root=0)

local_sum = np.sum(local_numbers)

print(f"Rank {rank}: local sum = {local_sum}")

global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Global sum = {global_sum}")
