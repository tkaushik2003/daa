from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    numbers = list(range(1, 11))
else:
    numbers = None

local_numbers = [0] * (10 // size)

comm.Scatter(numbers, local_numbers, root=0)

print("Process %d received: %s" % (rank, local_numbers))
