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