def obtener_fibonacci(n):

#    lista con los primeros números de la secuencia de Fibonacci.

    secuencia = []
    a = 0
    b = 1

    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b

    return secuencia


def main():
    entrada = input(
        "Ingrese los números Fibonacci: "
    )

    # separar los valores por coma (como si fuera una lista)
    valores = entrada.split(",")

    for valor in valores:
        valor = valor.strip()

        # confirmar que no es entero
        if not valor.isdigit():
            print(f"'{valor}' no es un número válido.")
            continue

        n = int(valor)

        if n <= 0:
            print(f"{n}: Valor inválido. Debe ser mayor que 0.")
            continue

        fibonacci = obtener_fibonacci(n)

        print(f"Fibonacci ({n}):", end=" ")
        for num in fibonacci:
            print(num, end=" ")
        print()

main()

