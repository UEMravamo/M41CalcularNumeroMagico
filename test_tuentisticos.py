import pytest
from numero_magico.tuentisticos import es_tuentistico, generar_numeros_tuentisticos


def test_es_tuentistico():
    assert es_tuentistico(20) is True
    assert es_tuentistico(19) is False

def test_generar_numeros_tuentisticos():
    assert generar_numeros_tuentisticos(30) == [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]