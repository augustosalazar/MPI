import os
import random
import shutil


def generar_spanish_words_info(output_file, target_size=2000):
    """
    Genera un archivo de vocabulario con palabras base, palabras técnicas
    y palabras sintéticas hasta alcanzar target_size.
    """
    base_words = [
        "de", "la", "que", "el", "en", "y", "a", "los", "se", "del",
        "las", "por", "un", "para", "con", "no", "una", "su", "al", "lo",
        "como", "mas", "pero", "sus", "le", "ya", "o", "este", "si", "porque",
        "esta", "entre", "cuando", "muy", "sin", "sobre", "tambien", "me", "hasta", "hay",
        "donde", "quien", "desde", "todo", "nos", "durante", "todos", "uno", "les", "ni",
        "contra", "otros", "ese", "eso", "ante", "ello", "e", "esto", "mi", "antes",
        "algunos", "unos", "yo", "otro", "otras", "otra", "tanto", "esa",
        "estos", "mucho", "quienes", "nada", "muchos", "cual", "poco", "ella", "estar", "estas",
        "algunas", "algo", "nosotros", "mis", "tu", "te", "ti", "tus", "ellas", "nosotras",
        "vosotros", "vosotras", "os", "mio", "mia", "mios", "mias", "tuyo", "tuya", "tuyos",
        "tuyas", "suyo", "suya", "suyos", "suyas", "nuestro", "nuestra", "nuestros", "nuestras",
        "vuestro", "vuestra", "vuestros", "vuestras"
    ]

    tech_words = [
        "archivo", "archivos", "directorio", "directorios", "carpeta", "carpetas",
        "documento", "documentos", "texto", "textos", "palabra", "palabras",
        "frase", "frases", "linea", "lineas", "parrafo", "parrafos",
        "consulta", "consultas", "busqueda", "busquedas", "resultado", "resultados",
        "conteo", "conteos", "frecuencia", "frecuencias", "ocurrencia", "ocurrencias",
        "termino", "terminos", "expresion", "expresiones", "token", "tokens",
        "indice", "indices", "lista", "listas", "coleccion", "colecciones",
        "conjunto", "conjuntos", "grupo", "grupos", "dato", "datos",
        "dataset", "datasets", "registro", "registros", "campo", "campos",
        "valor", "valores", "clave", "claves", "entrada", "entradas",
        "salida", "salidas", "proceso", "procesos", "hilo", "hilos",
        "nodo", "nodos", "cluster", "clusters", "servidor", "servidores",
        "cliente", "clientes", "worker", "workers", "scheduler", "schedulers",
        "maestro", "maestros", "esclavo", "esclavos", "memoria", "memorias",
        "latencia", "latencias", "ancho", "anchos", "banda", "bandas",
        "red", "redes", "paquete", "paquetes", "mensaje", "mensajes",
        "bloque", "bloques", "segmento", "segmentos", "particion", "particiones",
        "distribucion", "distribuciones", "paralelismo", "paralela", "paralelo",
        "secuencial", "sincrono", "asincrono", "sincronizacion", "coordinacion",
        "comunicacion", "transmision", "recepcion", "broadcast", "scatter", "gather",
        "reduce", "barrier", "rank", "size", "balance", "desbalance",
        "carga", "cargas", "asignacion", "asignaciones", "planificacion", "planificaciones",
        "ejecucion", "ejecuciones", "tiempo", "tiempos", "duracion", "duraciones",
        "velocidad", "velocidades", "aceleracion", "eficiencia", "rendimiento", "escalabilidad",
        "sobrecosto", "overhead", "serializacion", "deserializacion", "lectura", "lecturas",
        "escritura", "escrituras", "apertura", "cierre", "buffer", "buffers",
        "flujo", "flujos", "stream", "streams", "sistema", "sistemas",
        "modulo", "modulos", "funcion", "funciones", "metodo", "metodos",
        "rutina", "rutinas", "algoritmo", "algoritmos", "estructura", "estructuras",
        "vector", "vectores", "matriz", "matrices", "diccionario", "diccionarios",
        "hash", "mapa", "mapas", "tabla", "tablas", "contador",
        "contadores", "acumulador", "acumuladores", "agregacion", "agregaciones",
        "fusion", "fusiones", "mezcla", "mezclas", "combinacion", "combinaciones",
        "reduccion", "reducciones", "resumen", "resumenes", "estadistica", "estadisticas",
        "analisis", "analitica", "procesamiento", "preprocesamiento", "normalizacion",
        "limpieza", "filtrado", "tokenizacion", "comparacion", "comparaciones",
        "buscador", "indexacion", "coincidencia", "coincidencias", "relevancia",
        "ranking", "topico", "topicos", "terminologia", "vocabulario", "corpus",
        "frecuente", "infrecuente", "comun", "raro", "global", "local",
        "parcial", "final", "temporal", "permanente", "dinamico", "estatico",
        "manual", "automatico", "distribuido", "centralizado", "colectivo", "individual",
        "cooperativo", "independiente", "concurrente", "exactitud", "precision",
        "consistencia", "integridad", "robustez", "tolerancia", "fallo", "fallos",
        "error", "errores", "excepcion", "excepciones", "validacion", "verificacion",
        "prueba", "pruebas", "benchmark", "medicion", "mediciones", "metrica",
        "metricas", "monitor", "monitoreo", "perfil", "perfilado", "depuracion",
        "traza", "trazas", "bitacora", "evento", "eventos", "instancia",
        "instancias", "ejemplo", "ejemplos", "escenario", "escenarios", "caso",
        "casos", "lote", "lotes", "iteracion", "iteraciones", "ciclo",
        "ciclos", "repeticion", "repeticiones", "muestreo", "muestra", "muestras"
    ]

    prefixes = [
        "dato", "termino", "nodo", "archivo", "texto", "token", "indice",
        "vector", "matriz", "bloque", "segmento", "proceso", "worker",
        "tarea", "cluster", "consulta", "resultado", "evento", "registro",
        "paquete", "buffer", "modulo", "funcion", "mensaje", "prueba"
    ]

    words = []
    seen = set()

    def add_word(w):
        w = w.strip().lower()
        if w and w not in seen:
            seen.add(w)
            words.append(w)

    for w in base_words:
        add_word(w)

    for w in tech_words:
        add_word(w)

    i = 1
    while len(words) < target_size:
        for prefix in prefixes:
            add_word(f"{prefix}{i:04d}")
            if len(words) >= target_size:
                break
        i += 1

    with open(output_file, "w", encoding="utf-8") as f:
        for w in words:
            f.write(w + "\n")

    print(f"Vocabulario generado: {output_file}")
    print(f"Total de palabras en vocabulario: {len(words)}")


def asegurar_vocabulario(vocab_path, min_vocab_size=2000):
    """
    Si el archivo de vocabulario no existe, lo crea.
    Si existe pero tiene menos de min_vocab_size palabras únicas, lo regenera.
    """
    if not os.path.exists(vocab_path):
        print(f"No existe {vocab_path}. Se generará automáticamente.")
        generar_spanish_words_info(vocab_path, target_size=min_vocab_size)
        return

    with open(vocab_path, "r", encoding="utf-8") as f:
        vocab = [w.strip().lower() for w in f if w.strip()]
    vocab_unico = list(dict.fromkeys(vocab))

    if len(vocab_unico) < min_vocab_size:
        print(
            f"El vocabulario actual tiene {len(vocab_unico)} palabras únicas, "
            f"menos que el mínimo requerido ({min_vocab_size}). Se regenerará."
        )
        generar_spanish_words_info(vocab_path, target_size=min_vocab_size)
    else:
        print(f"Vocabulario existente encontrado con {len(vocab_unico)} palabras únicas.")


def cargar_vocabulario(word_list_path):
    with open(word_list_path, "r", encoding="utf-8") as f:
        vocab = [w.strip().lower() for w in f if w.strip()]
    vocab = list(dict.fromkeys(vocab))
    if not vocab:
        raise RuntimeError("El archivo de vocabulario está vacío.")
    return vocab


def elegir_tamano_archivo():
    """
    Genera tamaños heterogéneos:
    - 60% pequeños
    - 30% medianos
    - 10% grandes
    """
    r = random.random()
    if r < 0.60:
        return random.randint(2_000, 5_000)
    elif r < 0.90:
        return random.randint(10_000, 20_000)
    else:
        return random.randint(50_000, 100_000)


def generar_consulta(vocab, query_size, query_path):
    """
    Genera consulta.txt con palabras distintas del vocabulario.
    Si query_size > len(vocab), se limita al tamaño del vocabulario.
    """
    reales = min(query_size, len(vocab))
    consulta = random.sample(vocab, reales)

    with open(query_path, "w", encoding="utf-8") as f:
        for palabra in consulta:
            f.write(palabra + "\n")

    print(f"Creado consulta.txt con {reales} palabras")
    if query_size > len(vocab):
        print(
            f"Aviso: se solicitaron {query_size} palabras, "
            f"pero el vocabulario solo tiene {len(vocab)} palabras únicas."
        )


def preparar_directorio_salida(output_path):
    """
    Elimina completamente el directorio de salida si existe
    y luego lo vuelve a crear vacío.
    """
    if os.path.exists(output_path):
        print(f"Eliminando directorio existente: {output_path}")
        shutil.rmtree(output_path)

    os.makedirs(output_path, exist_ok=True)
    print(f"Directorio de salida listo: {output_path}")


def generar_textos_espanol(
    output_dir="dataset",
    num_files=1000,
    query_size=100,
    word_list_path="spanish_words.info",
    min_vocab_size=2000,
    weighted=False,
    seed=42
):
    """
    Genera:
    - un directorio con archivos de texto file_0001.txt, file_0002.txt, ...
    - un archivo consulta.txt con query_size palabras
    - un archivo de vocabulario si no existe o si es demasiado pequeño

    Si el directorio de salida ya existe, se elimina completamente antes
    de generar el nuevo dataset.
    """
    random.seed(seed)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    vocab_path = os.path.join(script_dir, word_list_path)
    output_path = os.path.join(script_dir, output_dir)

    asegurar_vocabulario(vocab_path, min_vocab_size=min_vocab_size)
    vocab = cargar_vocabulario(vocab_path)

    preparar_directorio_salida(output_path)

    weights = None
    if weighted:
        weights = [1 / (i + 1) for i in range(len(vocab))]

    query_path = os.path.join(output_path, "consulta.txt")
    generar_consulta(vocab, query_size, query_path)

    total_words = 0
    for i in range(1, num_files + 1):
        count = elegir_tamano_archivo()
        if weights:
            palabras = random.choices(vocab, weights=weights, k=count)
        else:
            palabras = random.choices(vocab, k=count)

        filename = f"file_{i:04d}.txt"
        path = os.path.join(output_path, filename)

        with open(path, "w", encoding="utf-8") as f_out:
            f_out.write(" ".join(palabras))

        total_words += count

        if i % 50 == 0 or i == num_files:
            print(f"Generados {i}/{num_files} archivos...")

    print("\nResumen:")
    print(f"- Carpeta de salida: {output_path}")
    print(f"- Archivo de vocabulario: {vocab_path}")
    print(f"- Archivos generados: {num_files}")
    print(f"- Total aproximado de palabras: {total_words}")
    print(f"- Vocabulario único disponible: {len(vocab)}")
    print(f"- Tamaño de consulta solicitado: {query_size}")
    print(f"- Modo ponderado: {weighted}")


if __name__ == "__main__":
    generar_textos_espanol(
        output_dir="dataset",
        num_files=3000,
        query_size=200,
        word_list_path="spanish_words.info",
        min_vocab_size=2000,
        weighted=True,
        seed=42
    )
