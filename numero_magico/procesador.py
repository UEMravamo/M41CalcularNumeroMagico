from functools import partial
from multiprocessing import Pool
from grafo_tuentistico import GrafoTuentistico, ExploradorGrafo
from utils import generar_numeros_tuentisticos


def procesar_casos_mapreduce(casos):
    """
    Procesa una lista de casos utilizando MapReduce y devuelve los resultados para cada caso.
    """
    casos_validos = [n for n in casos if 1 <= n <= 262]

    if len(casos_validos) != len(casos):
        print("Algunos casos no están en el rango permitido (1 ≤ N ≤ 262) y serán ignorados.")

    limite = max(casos_validos) if casos_validos else 0
    numeros_tuentisticos = generar_numeros_tuentisticos(limite)

    grafo = GrafoTuentistico(numeros_tuentisticos)
    explorador = ExploradorGrafo(grafo)

    # Usar Pool para realizar el mapeo paralelo
    with Pool() as pool:
        resultados = pool.map(partial(procesar_numero, explorador=explorador), enumerate(casos, start=1))

    return resultados


def procesar_numero(caso, explorador):
    """
    Procesa un número individualmente y determina el resultado utilizando el explorador del grafo.
    """
    indice, numero = caso
    resultado = explorador.buscar_maxima_suma(numero)
    return f"Case #{indice}: {resultado}"