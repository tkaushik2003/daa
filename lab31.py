from mpi4py import MPI
import random
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank==0:
    n = int(size)-1
    x = 33
    num = int(x/n)
    comm.send(num,dest=1,tag=11)
    comm.send(num,dest=2,tag=12)
    comm.send(num,dest=3,tag=13)
    list1=comm.recv(source=1,tag=1)
    list2=comm.recv(source=2,tag=2)
    list3=comm.recv(source=3,tag=3)
    result = list1+list2+list3
    for x in result:
        if x%5==0:
            print(x)
elif rank==1:
    y=comm.recv(source=0,tag=11)
    list=[]
    for i in range(0,y):
        tmp = random.randint(1,1000)
        list.append(tmp)
    comm.send(list,dest=0,tag=1)
elif rank==2:
    y=comm.recv(source=0,tag=12)
    list=[]
    for i in range(0,y):
        tmp = random.randint(1,1000)
        list.append(tmp)
    comm.send(list,dest=0,tag=2)
elif rank==3:
    y=comm.recv(source=0,tag=13)
    list=[]
    for i in range(0,y):
        tmp = random.randint(1,1000)
        list.append(tmp)
    comm.send(list,dest=0,tag=3)

