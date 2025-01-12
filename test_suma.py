import pytest
from numero_magico.suma_tuentisticos import maximo_elementos_suma_tuentistica

def test_maximo_elementos_suma_tuentistica():
    numeros_tuentisticos = [20, 21, 22]
    assert maximo_elementos_suma_tuentistica(80, numeros_tuentisticos) == 4
    assert maximo_elementos_suma_tuentistica(35, numeros_tuentisticos) == "IMPOSSIBLE"