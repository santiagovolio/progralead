import cesar

def menu():
    print("EJERCICIO 2: CESAR")
    print("1. Encriptar texto")
    print("2. Desencriptar texto")
    print("3. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        texto = input("Ingrese el texto a encriptar: ")
        n = int(input("Ingrese el desplazamiento: "))
        resultado = cesar.encriptar_cesar(texto, n)
        print("Texto encriptado:", resultado)

    elif opcion == "2":
        texto = input("Ingrese el texto a desencriptar: ")
        n = int(input("Ingrese el desplazamiento usado: "))
        resultado = cesar.desencriptar_cesar(texto, n)
        print("Texto original:", resultado)

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")