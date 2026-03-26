import csv
import json


def calcular_promedios(registros):
    cantidad = len(registros)

    if cantidad == 0:
        return None

    suma_edades = 0
    suma_salarios = 0
    suma_pesos = 0

    for persona in registros:
        suma_edades += float(persona["edad"])
        suma_salarios += float(persona["salario"])
        suma_pesos += float(persona["peso"])

    promedio_edad = suma_edades / cantidad
    promedio_salario = suma_salarios / cantidad
    promedio_peso = suma_pesos / cantidad

    return promedio_edad, promedio_salario, promedio_peso


def leer_csv(ruta):
    registros = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            registros.append(fila)

    return registros


def leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        registros = json.load(archivo)

    return registros


def mostrar_resultados(promedios):
    if promedios is None:
        print("No hay ningun archivo para calcular.")
        return

    promedio_edad, promedio_salario, promedio_peso = promedios
    
    print("-"*34)
    print(" RESULTADOS ")
    print("-"*34)
    print("Promedio de edad:", round(promedio_edad, 2))
    print("Promedio de salario:", round(promedio_salario, 2))
    print("Promedio de peso:", round(promedio_peso, 2))


def mostrar_menu():
    print("-"*34)
    print(" MENÚ ")
    print("-"*34)
    print("1. Leer archivo en formato CSV")
    print("2. Leer archivo en formato JSON")
    print("3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                datos = leer_csv("datos_personas/personas.csv")
                promedios = calcular_promedios(datos)
                mostrar_resultados(promedios)
            except FileNotFoundError:
                print("No se encontró el archivo personas.csv en la carpeta datos_personas.")
            except KeyError:
                print("Faltan columnas requeridas en el archivo.")
            except ValueError:
                print("Hay valores inválidos en el archivo.")

        elif opcion == "2":
            try:
                datos = leer_json("datos_personas/personas.json")
                promedios = calcular_promedios(datos)
                mostrar_resultados(promedios)
            except FileNotFoundError:
                print("No está el archivo personas.json")
            except KeyError:
                print("Faltan claves en el archivo")
            except ValueError:
                print("Hay valores inválidos en el archivo.")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción incorrecta.")


if __name__ == "__main__":
    main()