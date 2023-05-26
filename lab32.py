from mpi4py import MPI
import random
import math
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank==0:
    n = 2
    x = 1000
    
    arr = []
    for i in range(1000):
        a = random.randint(1,50)
        arr.append(a)
    num = int(math.ceil(len(arr)/n))    
    on = arr[:num+1]
    to = arr[num+1:(num+1)*2]
              
    comm.send(on,dest=1,tag=11)
    comm.send(arr,dest=2,tag=12)
    comm.send(to,dest=3,tag=13)
    list1=comm.recv(source=1,tag=1)
    list2=comm.recv(source=2,tag=2)
    list3=comm.recv(source=3,tag=3)
    result = list1+list2+list3
    print(result)
    
elif rank==1:
    y=comm.recv(source=0,tag=11)
    su1 = 0
    for i in y:
        if i%2!=0:
            su1 = su1+i
            
    comm.send(su1,dest=0,tag=1)
elif rank==2:
    y=comm.recv(source=0,tag=12)
    su2 = 0
    for i in y:
        if i%2==0:
            su2 = su2+i
    comm.send(su2,dest=0,tag=2)
elif rank==3:
    y=comm.recv(source=0,tag=13)
    su3 = 0
    for i in y:
        if i%2==0:
            su3 = su3+i
    comm.send(su3,dest=0,tag=3)
