from ejemplos.persona import Persona
from ejemplos.mascota import Mascota
from ejemplos.vehiculo import Vehiculo
from ejemplos.direccion import Direccion


def leer_entero(mensaje: str) -> int:
    while True:
        texto = input(mensaje).strip()
        try:
            return int(texto)
        except ValueError:
            print("Ingrese un número entero válido.")


def imprimir_lista(titulo: str, lista: list) -> None:
    print(f"\n--- {titulo} ---")
    if not lista:
        print("(No hay registros)")
        return
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")


def mostrar_menu() -> None:
    print("\nMENÚ - SIMULADOR DE VIDA")
    print("1. Crear persona")
    print("2. Crear mascota")
    print("3. Crear vehículo")
    print("4. Imprimir personas")
    print("5. Imprimir mascotas")
    print("6. Imprimir vehículos")
    print("7. Imprimir todas las entidades")
    print("8. Salir")


def elegir_persona(personas: list[Persona]) -> Persona | None:
    if not personas:
        return None

    print("\nSeleccione un propietario (o ENTER para ninguno):")
    for i, p in enumerate(personas, start=1):
        print(f"{i}. {p.nombre} (len={len(p)})")

    eleccion = input("Número: ").strip()
    if eleccion == "":
        return None

    try:
        idx = int(eleccion)
        if 1 <= idx <= len(personas):
            return personas[idx - 1]
    except ValueError:
        pass

    print("Selección inválida. Se guardará sin propietario.")
    return None


def main() -> None:
    personas: list[Persona] = []
    mascotas: list[Mascota] = []
    vehiculos: list[Vehiculo] = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            edad = leer_entero("Edad: ")
            ocupacion = input("Ocupación: ").strip()

            print("\nDirección (composición):")
            provincia = input("Provincia: ").strip()
            canton = input("Cantón: ").strip()
            distrito = input("Distrito: ").strip()

            direccion = Direccion(provincia, canton, distrito)
            personas.append(Persona(nombre, edad, ocupacion, direccion))
            print("Persona creada y guardada.")

        elif opcion == "2":
            nombre = input("Nombre: ").strip()
            especie = input("Especie: ").strip()
            edad = leer_entero("Edad: ")
            mascotas.append(Mascota(nombre, especie, edad))
            print("Mascota creada y guardada.")

        elif opcion == "3":
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            anio = leer_entero("Año: ")
            tipo = input("Tipo (carro/moto/etc.): ").strip()

            propietario = elegir_persona(personas)  # ASOCIACIÓN
            vehiculos.append(Vehiculo(marca, modelo, anio, tipo, propietario))
            print("Vehículo creado y guardado.")

        elif opcion == "4":
            imprimir_lista("PERSONAS", personas)

        elif opcion == "5":
            imprimir_lista("MASCOTAS", mascotas)

        elif opcion == "6":
            imprimir_lista("VEHÍCULOS", vehiculos)

        elif opcion == "7":
            imprimir_lista("PERSONAS", personas)
            imprimir_lista("MASCOTAS", mascotas)
            imprimir_lista("VEHÍCULOS", vehiculos)

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()