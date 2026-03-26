from figuras import Cubo, Paralelepipedo, Cilindro, Esfera, Cono
from liskov import imprimir_volumen

def menu():
    print("CALCULADORA DE VOLUMEN NUEVA")
    print("1. Volumen del cubo")
    print("2. Volumen del paralelepípedo")
    print("3. Volumen del cilindro")
    print("4. Volumen de la esfera")
    print("5. Volumen del cono")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lado = float(input("Ingrese el lado: "))
            figura = Cubo(lado)
            imprimir_volumen(figura)

        elif opcion == "2":
            l = float(input("Largo: "))
            b = float(input("Ancho: "))
            h = float(input("Alto: "))
            figura = Paralelepipedo(l, b, h)
            imprimir_volumen(figura)

        elif opcion == "3":
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            figura = Cilindro(r, h)
            imprimir_volumen(figura)

        elif opcion == "4":
            r = float(input("Radio: "))
            figura = Esfera(r)
            imprimir_volumen(figura)

        elif opcion == "5":
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            figura = Cono(r, h)
            imprimir_volumen(figura)

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()