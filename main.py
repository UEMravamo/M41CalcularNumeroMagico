def main():
    c = int(input("Introduce el numbero of casos: ").strip())
    results = []

    for case_number in range(1, c + 1):
        n = int(input(f"Introduce el numero de casos #{case_number}: ").strip())
        result = max_tuentistic_sum(n)
        results.append(f"Case #{case_number}: {result}")

    for result in results:
        print(result)

if __name__ == '__main__':
    main()