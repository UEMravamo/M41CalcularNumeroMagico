from tuentisticos import generar_numeros_tuentisticos
from suma_tuentisticos import maximo_elementos_suma_tuentistica

def procesar_casos(casos):
    """
    Procesa una lista de casos y devuelve los resultados para cada caso.
    """
    # Filtrar casos fuera del rango permitido
    casos_validos = [n for n in casos if 1 <= n <= 262]

    if len(casos_validos) != len(casos):
        print("Algunos casos no están en el rango permitido (1 ≤ N ≤ 262) y serán ignorados.")

    limite = max(casos_validos) if casos_validos else 0  # El límite más alto que necesitamos considerar
    numeros_tuentisticos = generar_numeros_tuentisticos(limite)

    resultados = []
    for i, numero in enumerate(casos, start=1):
        resultado = maximo_elementos_suma_tuentistica(numero, numeros_tuentisticos)
        resultados.append(f"Case #{i}: {resultado}")
    return resultados

if __name__ == "__main__":
    print("Introduce el número de casos entre 1 y 500:")
    valido = False  # Variable de control para salir del bucle
    cantidad_casos = 0

    while not valido:
        try:
            cantidad_casos = int(input().strip())
            if 1 <= cantidad_casos <= 500:
                valido = True  # Cambiar el estado para salir del bucle
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

    resultados = procesar_casos(casos)

    print("\nResultados:")
    for resultado in resultados:
        print(resultado)
