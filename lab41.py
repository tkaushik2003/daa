from mpi4py import MPI
import random
import math
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank==0:
    n=2
    fact = 10
    arr = []
    for i in range(1,fact+1):
        arr.append(i)
    num = int(math.ceil(len(arr)/n))    
    on =arr[:num+1]
    tw = arr[num+1:(num+1)*2]
    
              
    comm.send(on,dest=1,tag=11)
    comm.send(tw,dest=2,tag=12)
    
    list1=comm.recv(source=1,tag=1)
    list2=comm.recv(source=2,tag=2)
    
    result = list1*list2
    print(result)
    
elif rank==1:
    y=comm.recv(source=0,tag=11)
    mul1 = 1
    for i in y:
        
        mul1 = mul1*i
            
    comm.send(mul1,dest=0,tag=1)
elif rank==2:
    y=comm.recv(source=0,tag=12)
    mul2 = 1
    for i in y:
        mul2 = mul2*i
    comm.send(mul2,dest=0,tag=2)

