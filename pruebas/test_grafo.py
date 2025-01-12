import pytest
from numero_magico.grafo_tuentistico import GrafoTuentistico, ExploradorGrafo

def test_generar_vecinos():
    numeros_tuentisticos = [20, 21, 22]
    grafo = GrafoTuentistico(numeros_tuentisticos)

    # Nodo con vecinos válidos
    assert grafo.generar_vecinos(50) == [30, 29, 28]

    # Nodo sin vecinos válidos
    assert grafo.generar_vecinos(19) == []


def test_buscar_maxima_suma():
    numeros_tuentisticos = [20, 21]
    grafo = GrafoTuentistico(numeros_tuentisticos)
    explorador = ExploradorGrafo(grafo)

    # Caso posible
    assert explorador.buscar_maxima_suma(80) == 4  # 20 + 20 + 20 + 20

    # Caso imposible
    assert explorador.buscar_maxima_suma(19) == "IMPOSSIBLE"