def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Entrada inválida. Intente de nuevo.")


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")


def leer_flotante(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número válido.")


def leer_booleano(mensaje):
    while True:
        valor = input(mensaje + " (s/n): ").strip().lower()
        if valor == "s":
            return True
        elif valor == "n":
            return False
        else:
            print("Opción inválida. Escriba 's' o 'n'.")

