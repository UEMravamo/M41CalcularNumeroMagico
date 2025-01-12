from numero_magico.tuentisticos import es_tuentistico

def maximo_elementos_suma_tuentistica(numero, numeros_tuentisticos):
    """
    Calcula el número máximo de elementos que puede tener una suma tuentística de 'numero'
    usando un enfoque basado en grafos.
    """
    # Validar rango
    if not (1 <= numero <= 262):
        return "IMPOSSIBLE"

    # Si el número es tuentístico, devuelve 1
    if es_tuentistico(numero):
        return 1

    # Si el número es menor que el menor tuentístico, es imposible
    minimo_tuentistico = min(numeros_tuentisticos)
    if numero < minimo_tuentistico:
        return "IMPOSSIBLE"

    # Implementación tipo DFS para buscar el máximo número de pasos
    maximo_contador = 0
    pila = [(numero, 0)]  # (nodo actual, número de pasos)

    while pila:
        actual, contador = pila.pop()
        for t in numeros_tuentisticos:
            if actual - t == 0:  # Si llegamos exactamente a 0, actualizamos el máximo
                maximo_contador = max(maximo_contador, contador + 1)
            elif actual - t > 0:  # Si aún podemos restar, añadimos a la pila
                pila.append((actual - t, contador + 1))

    return maximo_contador if maximo_contador > 0 else "IMPOSSIBLE"