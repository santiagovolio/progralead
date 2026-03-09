import volumenes

def mostrar_menu():
    print("\nSeleccione la figura que desea calcular")
    print("1. Cubo")
    print("2. Paralelepípedo")
    print("3. Cilindro")
    print("4. Esfera")
    print("5. Cono")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        lado = float(input("Indique el lado del cubo: "))
        v = volumenes.volumen_cubo(lado)
        print("Volumen del cubo:", v)

    elif opcion == "2":
        largo = float(input("Largo: "))
        ancho = float(input("Ancho: "))
        alto = float(input("Alto: "))
        v = volumenes.volumen_paralelepipedo(largo, ancho, alto)
        print("Volumen del paralelepípedo:", v)

    elif opcion == "3":
        radio = float(input("Radio: "))
        altura = float(input("Altura: "))
        v = volumenes.volumen_cilindro(radio, altura)
        print("Volumen del cilindro:", v)

    elif opcion == "4":
        radio = float(input("Radio: "))
        v = volumenes.volumen_esfera(radio)
        print("Volumen de la esfera:", v)

    elif opcion == "5":
        radio = float(input("Radio: "))
        altura = float(input("Altura: "))
        v = volumenes.volumen_cono(radio, altura)
        print("Volumen del cono:", v)

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Esa opción no funciona, elija una del numero 1 al 6.")