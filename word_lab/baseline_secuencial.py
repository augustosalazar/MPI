import os
import time
from collections import Counter


def cargar_consulta(consulta_path, case_sensitive=False):
    """
    Lee consulta.txt y devuelve un conjunto de palabras objetivo.
    """
    if not os.path.isfile(consulta_path):
        raise FileNotFoundError(f"No se encontró el archivo de consulta: {consulta_path}")

    with open(consulta_path, "r", encoding="utf-8") as f:
        palabras = [line.strip() for line in f if line.strip()]

    if not case_sensitive:
        palabras = [w.lower() for w in palabras]

    return set(palabras)


def contar_palabras_en_corpus(dataset_dir, consulta_name="consulta.txt", case_sensitive=False):
    """
    Cuenta cuántas veces aparecen las palabras de consulta.txt
    en todos los archivos file_*.txt del directorio dataset_dir.
    """
    consulta_path = os.path.join(dataset_dir, consulta_name)
    palabras_objetivo = cargar_consulta(consulta_path, case_sensitive=case_sensitive)

    freq_global = Counter()
    archivos_procesados = 0
    total_tokens_leidos = 0

    for fname in os.listdir(dataset_dir):
        if not fname.startswith("file_") or not fname.endswith(".txt"):
            continue

        ruta = os.path.join(dataset_dir, fname)
        if not os.path.isfile(ruta):
            continue

        archivos_procesados += 1

        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                palabras = linea.split()

                if not case_sensitive:
                    palabras = [w.lower() for w in palabras]

                total_tokens_leidos += len(palabras)

                for w in palabras:
                    if w in palabras_objetivo:
                        freq_global[w] += 1

    return freq_global, archivos_procesados, total_tokens_leidos


def guardar_resultados_csv(resultados_path, freq_global):
    """
    Guarda el conteo global en CSV para comparar con MPI y Dask.
    """
    with open(resultados_path, "w", encoding="utf-8") as f:
        f.write("palabra,conteo\n")
        for palabra in sorted(freq_global):
            f.write(f"{palabra},{freq_global[palabra]}\n")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_dir = os.path.join(script_dir, "dataset")

    consulta_name = "consulta.txt"
    case_sensitive = False
    top_n = 10
    output_file = "baseline_results.csv"

    if not os.path.isdir(dataset_dir):
        print(f"Error: no existe la carpeta dataset en {dataset_dir}")
        return

    t0 = time.perf_counter()

    try:
        freq_global, archivos_procesados, total_tokens_leidos = contar_palabras_en_corpus(
            dataset_dir,
            consulta_name=consulta_name,
            case_sensitive=case_sensitive
        )
    except FileNotFoundError as e:
        print("Error:", e)
        return

    t1 = time.perf_counter()
    elapsed = t1 - t0

    total_ocurrencias = sum(freq_global.values())
    top_words = freq_global.most_common(top_n)

    resultados_path = os.path.join(dataset_dir, output_file)
    guardar_resultados_csv(resultados_path, freq_global)

    print(f"Tiempo de ejecución: {elapsed:.6f} segundos\n")
    print(f"Dataset procesado: {dataset_dir}")
    print(f"Archivo de consulta: {consulta_name}")
    print(f"Archivos procesados: {archivos_procesados}")
    print(f"Total de tokens leídos: {total_tokens_leidos}")
    print(f"Total de ocurrencias encontradas: {total_ocurrencias}")
    print(f"Resultados guardados en: {resultados_path}\n")

    print(f"Top {top_n} palabras de consulta en el corpus:")
    for palabra, cuenta in top_words:
        print(f"  {palabra}: {cuenta}")


if __name__ == "__main__":
    main()
