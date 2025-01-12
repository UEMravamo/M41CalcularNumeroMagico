import pytest
from numero_magico.procesador import procesar_casos_mapreduce, procesar_numero
from numero_magico.grafo_tuentistico import GrafoTuentistico, ExploradorGrafo

def test_procesar_numero():
    numeros_tuentisticos = [20, 21]
    grafo = GrafoTuentistico(numeros_tuentisticos)
    explorador = ExploradorGrafo(grafo)

    # Caso vÃ¡lido
    caso = (1, 40)
    resultado = procesar_numero(caso, explorador)
    assert resultado == "Case #1: 2"  # 20 + 20

    # Caso imposible
    caso = (2, 19)
    resultado = procesar_numero(caso, explorador)
    assert resultado == "Case #2: IMPOSSIBLE"

def test_procesar_casos_mapreduce():
    casos = [40, 19, 80]
    resultados_esperados = [
        "Case #1: 2",  # 20 + 20
        "Case #2: IMPOSSIBLE",
        "Case #3: 4"   # 20 + 20 + 20 + 20
    ]
    resultados = procesar_casos_mapreduce(casos)
    assert resultados == resultados_esperados