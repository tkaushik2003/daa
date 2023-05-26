from mpi4py import MPI
import numpy as np
import random
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank ==0:
    rnum = comm.recv(source = 3,tag = 31)
    print(rnum*rnum)
if rank == 1:
    
    rnum = np.random.randint(1,100)
    print(rnum)
    comm.send(rnum,dest = 2,tag=31)
if rank  ==2:
    rnum = comm.recv(source = 1,tag = 31)
    print(rnum*rnum)
if rank == 3:
    
    rnum = np.random.randint(1,100)
    print(rnum)
    comm.send(rnum,dest = 0,tag=31)
