# MPI & Dask Examples

Use augustosalazar/slim-mpi or augustosalazar/slim-mpi:2 (for macOS and windows) or augustosalazar/un_mpi_image:v5

To run and delete the container after execution:
```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/slim-mpi:2 mpiexec --allow-run-as-root -n 3 python /app/code0.py

docker run --rm -v "$(pwd)"/target:/app augustosalazar/slim-mpi:2 mpiexec --allow-run-as-root -n 3 python /app/code0.py
```


## Prime example

### Serial version
Busqueda de los primos con 5 dígitos
```bash
docker run --rm -v "$(pwd)"/target:/app augustosalazar/slim-mpi:2 mpiexec python /app/primeChecker.py 5
```

### MPI version
Busqueda de los primos con 5 dígitos usando MPI con 4 workers (con un batch size de 10)
```bash
docker run --rm -v "$(pwd)"/target:/app augustosalazar/slim-mpi:2 mpiexec --allow-run-as-root -n 4 python /app/primeCheckerMPI.py 5
```

###  Dask version
Busqueda de los primos con 5 dígitos usando Dask con 4 workers (con un batch size de 10)
```bash
docker run --rm -v "$(pwd)"/target:/app --network host daskdev/dask:latest python /app/primeCheckerDask.py 5 4
```

To install nano on Play with Docker:
apk --update add nano


## Shared Memory
```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/slim-mpi:2 mpiexec --allow-run-as-root -n 3 python /app/shared01.py
Proceso 2 de 3 iniciado.
Proceso 0 de 3 iniciado.
Proceso 1 de 3 iniciado.
Contenido del array compartido:
[ 0 10 20]
```