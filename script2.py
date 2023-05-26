from mpi4py import MPI
from numpy import random
import numpy as np
a=MPI.Wtime()
print("Welcome")
b=MPI.Wtime()

ts=b-a

comm=MPI.COMM_WORLD
xt=MPI.Wtime() 
rank=comm.Get_rank()

if rank==0:
    arr = np.random.randint(0, 100, 10)
    print(arr)
    count = 0
    for i in arr:
        if i<=50:
            count = count+1
    print(count)        
    
    comm.send(arr, dest=1, tag=1)
    suuu = comm.recv(source = 1,tag=2)
    print(suuu)
if rank==1:
    d=comm.recv(source=0, tag=1)
    su1 = 0
    for j in d:
        su1 = su1+j
    comm.send(su1,dest = 0, tag=2)        


if rank==0:
    y=MPI.Wtime()
    tp=y-xt
    sp=ts/tp
    eff=sp/2*100
    print("Speed up factor ", sp)
    print("Efficiency ", eff)
