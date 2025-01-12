import pytest
from numero_magico.utils import generar_numeros_tuentisticos

def test_generar_numeros_tuentisticos():
    # Caso con límite bajo
    assert generar_numeros_tuentisticos(25) == [20, 21, 22, 23, 24, 25]

    # Caso con límite exacto
    assert generar_numeros_tuentisticos(30) == [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

    # Caso sin tuentísticos
    assert generar_numeros_tuentisticos(19) == []