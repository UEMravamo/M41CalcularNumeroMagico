from procesador import procesar_casos_mapreduce

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