#TAREA 4 - ZOOLÓGICO SANTIAGO VOLIO

# IMPORTAR EMPLEADOS

from empleados.administrador import Administrador
from empleados.guardian import Guardian
from empleados.conserje import Conserje
from empleados.veterinario import Veterinario

# IMPORTAR MEDIOS DE TRANSPORTE

from transportes.bicicleta import Bicicleta
from transportes.cuadraciclo import Cuadraciclo
from transportes.patineta import Patineta

# IMPORTAR ANIMALES
from animales.reptil import Reptil
from animales.mamifero import Mamifero
from animales.ave import Ave
from animales.pez import Pez
from animales.anfibio import Anfibio

#IMPORTAR SUBCATEGORÍAS DE ANIMALES (CLASES HIJAS)

from animales.leon import Leon
from animales.tiburon import Tiburon
from animales.cocodrilo import Cocodrilo
from animales.aguila import Aguila
from animales.rana import Rana

# IMPORTAR FUNCIONES DE LECTURA DE DATOS
from utilidades import leer_texto, leer_entero, leer_flotante, leer_booleano


empleados = []
transportes = []
animales = []


def agregar_administrador():
    try:
        empleado = Administrador(
            leer_texto("Cédula: "),
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 1),
            leer_flotante("Salario: ", 0),
            leer_texto("Área: ")
        )
        empleados.append(empleado)
        print("Administrador agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_guardian():
    try:
        empleado = Guardian(
            leer_texto("Cédula: "),
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 1),
            leer_flotante("Salario: ", 0),
            leer_texto("Zona asignada: ")
        )
        empleados.append(empleado)
        print("Guardián agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_conserje():
    try:
        empleado = Conserje(
            leer_texto("Cédula: "),
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 1),
            leer_flotante("Salario: ", 0),
            leer_texto("Turno: ")
        )
        empleados.append(empleado)
        print("Conserje agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_veterinario():
    try:
        empleado = Veterinario(
            leer_texto("Cédula: "),
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 1),
            leer_flotante("Salario: ", 0),
            leer_texto("Especialidad: ")
        )
        empleados.append(empleado)
        print("Veterinario agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def listar_empleados():
    if not empleados:
        print("No hay empleados registrados.")
        return
    print("-" * 30)
    print("LISTA DE EMPLEADOS")
    print("-" * 30)
    for empleado in empleados:
        print(empleado)


def agregar_bicicleta():
    try:
        transporte = Bicicleta(
            leer_texto("Placa: "),
            leer_texto("Marca: "),
            leer_flotante("Velocidad máxima: ", 1),
            leer_texto("Tipo de bicicleta: ")
        )
        transportes.append(transporte)
        print("Bicicleta agregada correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_cuadraciclo():
    try:
        transporte = Cuadraciclo(
            leer_texto("Placa: "),
            leer_texto("Marca: "),
            leer_flotante("Velocidad máxima: ", 1),
            leer_texto("Tipo de combustible: ")
        )
        transportes.append(transporte)
        print("Cuadraciclo agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_patineta():
    try:
        transporte = Patineta(
            leer_texto("Placa: "),
            leer_texto("Marca: "),
            leer_flotante("Velocidad máxima: ", 1),
            leer_booleano("¿Es eléctrica?")
        )
        transportes.append(transporte)
        print("Patineta agregada correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def listar_transportes():
    if not transportes:
        print("No hay medios de transporte registrados.")
        return
    print("-" * 30)
    print("LISTA DE TRANSPORTES")
    print("-" * 30)
    for transporte in transportes:
        print(transporte)


def agregar_reptil():
    try:
        animal = Reptil(
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 0),
            leer_flotante("Peso: ", 0.1),
            leer_texto("Hábitat: "),
            leer_booleano("¿Es venenoso?")
        )
        animales.append(animal)
        print("Reptil agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_mamifero():
    try:
        animal = Mamifero(
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 0),
            leer_flotante("Peso: ", 0.1),
            leer_texto("Hábitat: "),
            leer_texto("Dieta: ")
        )
        animales.append(animal)
        print("Mamífero agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_ave():
    try:
        animal = Ave(
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 0),
            leer_flotante("Peso: ", 0.1),
            leer_texto("Hábitat: "),
            leer_booleano("¿Puede volar?")
        )
        animales.append(animal)
        print("Ave agregada correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_pez():
    try:
        animal = Pez(
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 0),
            leer_flotante("Peso: ", 0.1),
            leer_texto("Hábitat: "),
            leer_booleano("¿Es de agua dulce?")
        )
        animales.append(animal)
        print("Pez agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def agregar_anfibio():
    try:
        animal = Anfibio(
            leer_texto("Nombre: "),
            leer_entero("Edad: ", 0),
            leer_flotante("Peso: ", 0.1),
            leer_texto("Hábitat: "),
            leer_booleano("¿Tiene piel húmeda?")
        )
        animales.append(animal)
        print("Anfibio agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def listar_animales():
    if not animales:
        print("No hay animales registrados.")
        return
    print("-" * 30)
    print("LISTA DE ANIMALES")
    print("-" * 30)
    for animal in animales:
        print(animal)


def cargar_ejemplos_especies():
    """
    Este es una lista de animales para facilitar las pruebas del sistema 
    sin necesidad de ingresar datos manualmente, así se puede probar el programa sin necesidad de
    ingresar datos a cada rato y para que
    sea más fácil de probar, pero no es necesario tenerlo.
    """
    animales.append(Leon("Simba", 5, 190, "Sabana", "Carnívoro", True))
    animales.append(Tiburon("Tiburoncín", 8, 600, "Acuario", False, 300))
    animales.append(Cocodrilo("Lilo", 12, 450, "Pantano", False, 4.2))
    animales.append(Aguila("Colmillo", 4, 6.5, "Jaula", True, 2.1))
    animales.append(Rana("René", 2, 0.8, "Ranario", True, "Verde"))


def submenu_empleados():
    while True:
        print("-"*30)
        print(" EMPLEADOS ")
        print("-"*30)
        print("  ")
        print("1. Agregar Administrador")
        print("2. Agregar Guardián")
        print("3. Agregar Conserje")
        print("4. Agregar Veterinario")
        print("5. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_administrador()
        elif opcion == "2":
            agregar_guardian()
        elif opcion == "3":
            agregar_conserje()
        elif opcion == "4":
            agregar_veterinario()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")


def submenu_transportes():
    while True:
        print("-"*30)
        print("TRANSPORTES")
        print("-"*30)
        print("  ")
        print("1. Agregar Bicicleta")
        print("2. Agregar Cuadraciclo")
        print("3. Agregar Patineta")
        print("4. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_bicicleta()
        elif opcion == "2":
            agregar_cuadraciclo()
        elif opcion == "3":
            agregar_patineta()
        elif opcion == "4":
            break
        else:
            print("Opción inválida, intente otra vez.")


def submenu_animales():
    while True:
        print("-"*30)
        print(" ANIMALES ")
        print("-"*30)
        print("  ")
        print("1. Agregar Reptil")
        print("2. Agregar Mamífero")
        print("3. Agregar Ave")
        print("4. Agregar Pez")
        print("5. Agregar Anfibio")
        print("6. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_reptil()
        elif opcion == "2":
            agregar_mamifero()
        elif opcion == "3":
            agregar_ave()
        elif opcion == "4":
            agregar_pez()
        elif opcion == "5":
            agregar_anfibio()
        elif opcion == "6":
            break
        else:
            print("Opción inválida, intente otra vez.")


def menu_principal():
    while True:
        print("-"*30)
        print("ADMINISTRADOR DE ZOOLÓGICO ")
        print("-"*30)
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Agregar medio de transporte")
        print("4. Listar medios de transporte")
        print("5. Agregar animal")
        print("6. Listar animales")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            submenu_empleados()
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            submenu_transportes()
        elif opcion == "4":
            listar_transportes()
        elif opcion == "5":
            submenu_animales()
        elif opcion == "6":
            listar_animales()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente otra vez.")


if __name__ == "__main__":
    cargar_ejemplos_especies()
    menu_principal()