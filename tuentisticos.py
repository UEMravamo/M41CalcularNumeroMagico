try:
    import inflect
except ImportError:
    print("Error: El módulo 'inflect' no está instalado. Instálalo ejecutando 'pip install inflect'.")
    exit(1)

def es_tuentistico(numero):
    """
    Verifica si un número es tuentístico (contiene "twenty" en su representación en inglés).
    """
    motor = inflect.engine()
    numero_en_ingles = motor.number_to_words(numero)
    return "twenty" in numero_en_ingles

def generar_numeros_tuentisticos(limite):
    """
    Genera una lista de todos los números tuentísticos menores o iguales al límite dado.
    """
    return [n for n in range(20, limite + 1) if es_tuentistico(n)]