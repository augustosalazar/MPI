from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

message = f"¡Hola desde el proceso {rank} de {size}!"
print(message)