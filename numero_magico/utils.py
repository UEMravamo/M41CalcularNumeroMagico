import inflect

def generar_numeros_tuentisticos(limite):
    """
    Genera una lista de todos los números tuentísticos menores o iguales al límite dado.
    """
    motor = inflect.engine()
    return [n for n in range(20, limite + 1) if "twenty" in motor.number_to_words(n)]