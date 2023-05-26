from mpi4py import MPI

a=MPI.Wtime()
print("Welcome")
b=MPI.Wtime()

ts=b-a

comm=MPI.COMM_WORLD
xt=MPI.Wtime() 
rank=comm.Get_rank()

if rank==0:
    x = [1,2,3,4,5,6,7]
    su = 0
    for i in x:
        su = su+i
    print(su)    
    comm.send(x, dest=1, tag=1)
    comm.send(x, dest=2)
if rank==1:
    d=comm.recv(source=0, tag=1)
    su1 = 0
    for j in d:
        if j%2==0:
            su1 = su1+j
    print("even sum",su1)        
if rank==2:
    b=comm.recv(source=0)
    su2 = 0
    for k in b:
        if k%2!=0:
            su2 = su2+k
    print("odd sum",su2) 

if rank==0:
    y=MPI.Wtime()
    tp=y-xt
    sp=ts/tp
    eff=sp/2*100
    print("Speed up factor ", sp)
    print("Efficiency ", eff)
