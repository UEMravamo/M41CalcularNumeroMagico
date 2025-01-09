from num2words import num2words
import sys

def es_tuentistico(num):
   
    return "twenty" in num2words(num)

def suma_max_tuentistica(n):
    
    # Generar lista de números tuentísticos menores o iguales a n
    numeros_tuentisticos = [i for i in range(1, n + 1) if es_tuentistico(i)]

    if not numeros_tuentisticos:
        return "IMPOSSIBLE"

    total = 0
    cont = 0

    # Intentamos sumar los números más grandes antes
    for total_num in sorted(numeros_tuentisticos, reverse=True):
        while total + total_num <= n:    
            total += total_num
            cont += 1
        if total == n:
            return cont

    return "IMPOSSIBLE"

def main():
   
    input_lines = sys.stdin.read().strip().split("\n")
    c = int(input_lines[0])

    resultados = []

    for case_number in range(1, c + 1):
        n = int(input_lines[case_number])
        resultado = suma_max_tuentistica(n)
        resultados.append(f"Case #{case_number}: {resultado}")

    print("\n".join(resultados))

if __name__ == "__main__":
    main()