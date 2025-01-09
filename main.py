import sys
try:
    import inflect
except ImportError:
    print("Error: El módulo 'inflect' no está instalado. Instálalo ejecutando 'pip install inflect'.")
    exit(1)

def es_tuentistico(num):
    motor = inflect.engine()
    num_en_ingles = motor.number_to_words(num)
    return "twenty" in num_en_ingles

def generar_numeros_tuentisticos(limite):
    return [n for n in range(20, limite + 1) if es_tuentistico(n)]

def suma_max_tuentistica(numero, numeros_tuentisticos):
    if es_tuentistico(numero):
        return 1

    minimo_tuentistico = min(numeros_tuentisticos)
    if numero < minimo_tuentistico:
        return "IMPOSSIBLE"

    maximo_contador = 0
    pila = [(numero, 0)]
    
    while pila:
        actual, contador = pila.pop()
        for t in numeros_tuentisticos:
            if actual - t == 0:
                maximo_contador = max(maximo_contador, contador + 1)
            elif actual - t > 0:
                pila.append((actual - t, contador + 1))
    
    return maximo_contador if maximo_contador > 0 else "IMPOSSIBLE"

def main():
    input_lines = sys.stdin.read().strip().split("\n")
    c = int(input_lines[0])

    resultados = []

    for case_number in range(1, c + 1):
        n = int(input_lines[case_number])
        resultado = suma_max_tuentistica(n)
        resultados.append(f"Case #{case_number}: {resultado}")

    print("\n".join(resultados))

if __name__ == '__main__':