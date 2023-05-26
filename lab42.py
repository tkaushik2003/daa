from mpi4py import MPI
import random
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank ==0:
    matrix = np.random.randint(10,size=(4,4))
    print(matrix)        
    a, b, c, d = split(matrix,2,2)
    print(a,b,c,d)
if rank == 1:
    pass
if rank  ==2:
    pass
if rank == 3:
    
    rnum = 10
    
