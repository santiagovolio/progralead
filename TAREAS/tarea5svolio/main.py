# TAREA # 5 - AGENDA DE CONTACTOS CON CSV Y JSON DE SHERLOCK HOLMES - SANTIAGO VOLIO 

import csv
import json

# Aquí defino los campos que debe tener cada contacto.
# para que los contactos sigan el mismo orden cuando se guarden en CSV.
CAMPOS = ["nombre", "telefono", "email", "edad", "residencia"]


def cargar_csv(nombre_archivo):

    contactos = []

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Leer cada fila del archivo CSV.
            for fila in lector:
                # Aquí construyo un diccionario por cada contacto.
                contacto = {
                    "nombre": fila["nombre"],
                    "telefono": fila["telefono"],
                    "email": fila["email"],
                    "edad": int(fila["edad"]),
                    "residencia": fila["residencia"]
                }

                # Agregar el contacto nuevo a la lista general.
                contactos.append(contacto)

    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo .CSV: {e}")

    return contactos


def cargar_json(nombre_archivo):
    # Funcion para leer .json
    contactos = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contactos = json.load(archivo)
            for contacto in contactos:
                contacto["edad"] = int(contacto["edad"])

    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")
    except json.JSONDecodeError:
        print("El archivo .JSON no tiene un formato válido.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo .JSON: {e}")

    return contactos


def guardar_csv(nombre_archivo, contactos):
    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()

            for contacto in contactos:
                escritor.writerow(contacto)

        print(f"Los contactos se guardaron correctamente en {nombre_archivo}.")

    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo .CSV: {e}")


def guardar_json(nombre_archivo, contactos):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(contactos, archivo, ensure_ascii=False, indent=4)

        print(f"Los contactos se guardaron correctamente en {nombre_archivo}.")

    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo JSON: {e}")


def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos para mostrar.")
        return
    print("-" * 30)
    print(" LISTA DE CONTACTOS ")
    print("-" * 30)

    # Enumerar contactos para mostrar la cantidad y el número de cada uno.
    for i, contacto in enumerate(contactos, start=1):
        print(f"\nContacto #{i}")
        print(f"Nombre: {contacto['nombre']}")
        print(f"Teléfono: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")
        print(f"Edad: {contacto['edad']}")
        print(f"Residencia: {contacto['residencia']}")


def buscar_contacto(contactos, nombre_buscar):
    # En esta función busco un contacto por nombre.
    # Debe de poder buscar sin importar mayúsculas o minúsculas, por eso uso .lower(), para que sea parcial
    resultados = []
    for contacto in contactos:
        if nombre_buscar.lower() in contacto["nombre"].lower():
            resultados.append(contacto)
    return resultados


def buscar_contacto_por_telefono(contactos, telefono_buscar):
    resultados = []
    for contacto in contactos:
        if telefono_buscar in contacto["telefono"]:
            resultados.append(contacto)
    return resultados


def agregar_contacto(contactos):
    # En esta función le pido al usuario los datos
    # para crear un contacto nuevo.
    print("-" * 30)
    print(" AGREGAR CONTACTO ")
    print("-" * 30)

    nombre = input("Ingrese el nombre: ").strip()
    telefono = input("Ingrese el teléfono: ").strip()
    email = input("Ingrese el email: ").strip()

    while True:
        edad_texto = input("Ingrese la edad: ").strip()
        if edad_texto.isdigit():
            edad = int(edad_texto)
            break
        print("La edad debe ser un número entero.")

    residencia = input("Ingrese la residencia: ").strip()

    # Construir el nuevo contacto con los datos ingresados.
    nuevo_contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "edad": edad,
        "residencia": residencia
    }

    # Agregar contacto a la lista
    contactos.append(nuevo_contacto)
    print("Contacto agregado correctamente.")


def seleccionar_archivo():
    print("Seleccione el tipo de archivo con el que desea trabajar:")
    print("1. CSV")
    print("2. JSON")

    while True:
        opcion = input("Opción: ").strip()

        if opcion == "1":
            return "csv", "contactos.csv"
        elif opcion == "2":
            return "json", "contactos.json"
        else:
            print("Opción inválida. Intente de nuevo.")


def cargar_contactos_segun_formato(tipo_archivo, nombre_archivo):
    if tipo_archivo == "csv":
        return cargar_csv(nombre_archivo)
    elif tipo_archivo == "json":
        return cargar_json(nombre_archivo)

    return []


def guardar_contactos_segun_formato(tipo_archivo, nombre_archivo, contactos):
    if tipo_archivo == "csv":
        guardar_csv(nombre_archivo, contactos)
    elif tipo_archivo == "json":
        guardar_json(nombre_archivo, contactos)


def mostrar_promedio_edades(contactos):
    if not contactos:
        print("No hay contactos cargados.")
        return

    suma_edades = 0
    for contacto in contactos:
        suma_edades += contacto["edad"]

    promedio = suma_edades / len(contactos)
    print(f"El promedio de edad de los contactos es: {promedio:.2f}")


def menu():
    tipo_archivo = None
    nombre_archivo = None
    contactos = []

    while True:
        print("-" * 49)
        print(" CARGAR AGENDA PARA INGRESAR AL MENÚ PRINCIPAL ")
        print("-" * 49)
        print("1. Cargar contactos desde archivo")
        print("2. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            tipo_archivo, nombre_archivo = seleccionar_archivo()
            contactos = cargar_contactos_segun_formato(tipo_archivo, nombre_archivo)
            print(f"\nSe cargó la agenda desde el archivo {nombre_archivo}.")
            print(f"Cantidad de contactos cargados: {len(contactos)}")
            break

        elif opcion == "2":
            print("Saliendo del programa.")
            return

        else:
            print("Opción inválida. Intente de nuevo.")

    while True:
        print("-" * 30)
        print(" MENÚ PRINCIPAL ")
        print("-" * 30)
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Buscar contacto por teléfono")
        print("4. Mostrar el promedio de edad de los contactos")
        print("5. Mostrar todos los contactos cargados")
        print("6. Guardar cambios")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_contacto(contactos)
            guardar_contactos_segun_formato(tipo_archivo, nombre_archivo, contactos)

        elif opcion == "2":
            nombre_buscar = input("Ingrese el nombre a buscar: ").strip()
            resultados = buscar_contacto(contactos, nombre_buscar)

            if resultados:
                print("-" * 30)
                print(" CONTACTOS ENCONTRADOS ")
                print("-" * 30)
                for contacto in resultados:
                    print(f"Nombre: {contacto['nombre']}")
                    print(f"Teléfono: {contacto['telefono']}")
                    print(f"Email: {contacto['email']}")
                    print(f"Edad: {contacto['edad']}")
                    print(f"Residencia: {contacto['residencia']}")
                    print("-" * 30)
            else:
                print("Ese contacto no existe.")

        elif opcion == "3":
            telefono_buscar = input("Ingrese el teléfono a buscar: ").strip()
            resultados = buscar_contacto_por_telefono(contactos, telefono_buscar)

            if resultados:
                print("-" * 30)
                print(" CONTACTOS ENCONTRADOS ")
                print("-" * 30)
                for contacto in resultados:
                    print(f"Nombre: {contacto['nombre']}")
                    print(f"Teléfono: {contacto['telefono']}")
                    print(f"Email: {contacto['email']}")
                    print(f"Edad: {contacto['edad']}")
                    print(f"Residencia: {contacto['residencia']}")
                    print("-" * 30)
            else:
                print("Ese contacto no existe.")

        elif opcion == "4":
            mostrar_promedio_edades(contactos)

        elif opcion == "5":
            mostrar_contactos(contactos)

        elif opcion == "6":
            guardar_contactos_segun_formato(tipo_archivo, nombre_archivo, contactos)

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()