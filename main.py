from num2words import num2words
import sys

def es_tuentistico(num):

    return "twenty" in num2words(num)

def sumaMaxTuentistica(n):

    numerosTuentistico = [i for i in range(1, n + 1) if es_tuentistico(i)]

    if not numerosTuentistico:
        return "IMPOSSIBLE"

    cont = 0
    total = 0
    for t_num in sorted(numerosTuentistico, reverse=True):
        while total + t_num <= n:    
            total += t_num
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
        resultado = sumaMaxTuentistica(n)
        resultados.append(f"Case #{case_number}: {resultado}")

    for resultado in resultados:
        print(resultado)

if __name__ == "_main_":
   main()