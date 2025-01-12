from multiprocessing import Pool
from functools import partial

class GrafoTuentistico:
    def __init__(self, numeros_tuentisticos):
        """
        Inicializa el grafo con los nodos representados por números tuentísticos.
        """
        self.numeros_tuentisticos = numeros_tuentisticos

    def generar_vecinos(self, nodo):
        """
        Genera los nodos vecinos restando números tuentísticos válidos.
        """
        return [nodo - t for t in self.numeros_tuentisticos if nodo - t >= 0]

class ExploradorGrafo:
    def __init__(self, grafo):
        """
        Inicializa el explorador del grafo.
        """
        self.grafo = grafo

    def buscar_maxima_suma(self, numero):
        """
        Realiza una búsqueda en profundidad (DFS) para encontrar el máximo número de pasos.
        """
        pila = [(numero, 0)]  # (nodo actual, número de pasos)
        maximo_contador = 0

        while pila:
            actual, contador = pila.pop()
            for vecino in self.grafo.generar_vecinos(actual):
                if vecino == 0:
                    maximo_contador = max(maximo_contador, contador + 1)
                else:
                    pila.append((vecino, contador + 1))

        return maximo_contador if maximo_contador > 0 else "IMPOSSIBLE"

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

def generar_numeros_tuentisticos(limite):
    """
    Genera una lista de todos los números tuentísticos menores o iguales al límite dado.
    """
    import inflect
    motor = inflect.engine()
    return [n for n in range(20, limite + 1) if "twenty" in motor.number_to_words(n)]

if __name__ == "__main__":
    print("Introduce el número de casos entre 1 y 500:")
    valido = False
    cantidad_casos = 0

    while not valido:
        try:
            cantidad_casos = int(input().strip())
            if 1 <= cantidad_casos <= 500:
                valido = True
            else:
                print("El número de casos debe estar entre 1 y 500. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    casos = []

    print(f"Introduce los {cantidad_casos} números, uno por línea:")
    for _ in range(cantidad_casos):
        numero = int(input().strip())
        if 1 <= numero <= 262:
            casos.append(numero)
        else:
            print(f"El número {numero} no está en el rango permitido. Por favor, inténtalo de nuevo.")

    resultados = procesar_casos_mapreduce(casos)

    print("\nResultados:")
    for resultado in resultados:
        print(resultado)