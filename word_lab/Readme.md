# Word Lab

This repository contains a Python script that generates text files with random Spanish words. The generated files can be used for various purposes, such as testing, data analysis, or language learning.

## Usage
To generate the text files, run the `generator.py` script. 

```bash
python generator.py
```

To run with docker

```bash
docker run --rm -v "$(pwd)":/app augustosalazar/slim-mpi:2 python /app/generator.py
```

  or for windows command prompt:

```bash
docker run --rm -v "%cd%:/app" augustosalazar/slim-mpi:2 python /app/generator.py
```


The script will create a specified number of text files in the `dataset` directory, each containing a random selection of Spanish words. The words are sourced from the `spanish_words.info` file, which should be placed in the same directory as the script.

On baseline_secuencial.py you can find a sequential implementation that goes through the consulta.txt file and seraches each of its words on the rest of the files to find the top 10 most common words


```bash
python baseline_secuencial.py
```

To run with docker

```bash
docker run --rm -v "$(pwd)":/app augustosalazar/slim-mpi:2 python /app/baseline_secuencial.py
```

or for windows command prompt:

```bash
docker run --rm -v "%cd%:/app" augustosalazar/slim-mpi:2 python /app/baseline_secuencial.py
```

A sample of the output:

```bash
~/development/MPI/word_lab python3 baseline_secuencial.py
Tiempo de ejecución: 5.271514 segundos

Dataset procesado: /Users/augustosalazar/development/MPI/word_lab/dataset
Archivo de consulta: consulta.txt
Archivos procesados: 3000
Total de tokens leídos: 44951458
Total de ocurrencias encontradas: 3631778
Resultados guardados en: /Users/augustosalazar/development/MPI/word_lab/dataset/baseline_results.csv

Top 10 palabras de consulta en el corpus:
  a: 785774
  para: 392156
  sus: 228913
  otros: 105530
  ante: 99832
  unos: 88794
  otra: 83901
  vosotros: 61617
  mios: 58420
  tuya: 56635
```

A batch script is provided to run all the experiments automatically:

```bash
docker run --rm -v "$(pwd)":/app augustosalazar/slim-mpi:2 sh /app/run_all.sh
```

or for windows command prompt:

```bash
docker run --rm -v "%cd%:/app" augustosalazar/slim-mpi:2 sh /app/run_all.sh
```

