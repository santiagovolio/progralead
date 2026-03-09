# TAREA 2 PROGRA 1 SANTIAGO VOLIO

#Lista de personas base
personas = [
    {
        "identificacion": "1-101-000001",
        "nombre": "María",
        "apellido": "González",
        "edad": 22,
        "salario": 450000,
        "ocupacion": "Estudiante",
        "altura": 1.62,
        "peso": 58.5
    },
    {
        "identificacion": "1-102-000002",
        "nombre": "Carlos",
        "apellido": "Ramírez",
        "edad": 31,
        "salario": 850000,
        "ocupacion": "Desarrollador",
        "altura": 1.75,
        "peso": 82.3
    },
    {
        "identificacion": "2-201-000003",
        "nombre": "Sofía",
        "apellido": "Vargas",
        "edad": 27,
        "salario": 620000,
        "ocupacion": "Diseñadora",
        "altura": 1.68,
        "peso": 60.0
    },
    {
        "identificacion": "3-301-000004",
        "nombre": "José",
        "apellido": "Cordero",
        "edad": 45,
        "salario": 1200000,
        "ocupacion": "Administrador",
        "altura": 1.80,
        "peso": 90.2
    },
    {
        "identificacion": "1-103-000005",
        "nombre": "Laura",
        "apellido": "Jiménez",
        "edad": 29,
        "salario": 710000,
        "ocupacion": "Contadora",
        "altura": 1.60,
        "peso": 55.1
    },
    {
        "identificacion": "4-401-000006",
        "nombre": "Andrés",
        "apellido": "Solís",
        "edad": 38,
        "salario": 980000,
        "ocupacion": "Ingeniero",
        "altura": 1.77,
        "peso": 78.6
    },
    {
        "identificacion": "2-202-000007",
        "nombre": "Valentina",
        "apellido": "Mora",
        "edad": 19,
        "salario": 380000,
        "ocupacion": "Asistente",
        "altura": 1.55,
        "peso": 49.4
    },
    {
        "identificacion": "5-501-000008",
        "nombre": "Diego",
        "apellido": "Pérez",
        "edad": 33,
        "salario": 900000,
        "ocupacion": "Analista",
        "altura": 1.73,
        "peso": 74.8
    },
    {
        "identificacion": "1-104-000009",
        "nombre": "Fernanda",
        "apellido": "Castro",
        "edad": 41,
        "salario": 1100000,
        "ocupacion": "Profesora",
        "altura": 1.66,
        "peso": 63.9
    },
    {
        "identificacion": "6-601-000010",
        "nombre": "Miguel",
        "apellido": "Alvarado",
        "edad": 26,
        "salario": 560000,
        "ocupacion": "Técnico",
        "altura": 1.70,
        "peso": 69.0
    },
    {
        "identificacion": "7-701-000011",
        "nombre": "Paula",
        "apellido": "Hernández",
        "edad": 24,
        "salario": 520000,
        "ocupacion": "Mercadóloga",
        "altura": 1.63,
        "peso": 57.2
    },
    {
        "identificacion": "1-105-000012",
        "nombre": "Ricardo",
        "apellido": "Paniagua",
        "edad": 50,
        "salario": 1500000,
        "ocupacion": "Gerente",
        "altura": 1.82,
        "peso": 95.5
    },
    {
        "identificacion": "8-801-000013",
        "nombre": "Gabriela",
        "apellido": "Salazar",
        "edad": 36,
        "salario": 870000,
        "ocupacion": "Enfermera",
        "altura": 1.58,
        "peso": 61.0
    },
    {
        "identificacion": "2-203-000014",
        "nombre": "Kevin",
        "apellido": "Arias",
        "edad": 28,
        "salario": 640000,
        "ocupacion": "Soporte TI",
        "altura": 1.74,
        "peso": 76.3
    },
    {
        "identificacion": "9-901-000015",
        "nombre": "Daniela",
        "apellido": "Chaves",
        "edad": 32,
        "salario": 730000,
        "ocupacion": "Arquitecta",
        "altura": 1.69,
        "peso": 62.8
    },
     {
        "identificacion": "1-106-000016",
        "nombre": "Natalia",
        "apellido": "Rojas",
        "edad": 21,
        "salario": 410000,
        "ocupacion": "Recepcionista",
        "altura": 1.60,
        "peso": 54.6
    },
    {
        "identificacion": "3-302-000017",
        "nombre": "Esteban",
        "apellido": "Méndez",
        "edad": 40,
        "salario": 1050000,
        "ocupacion": "Abogado",
        "altura": 1.78,
        "peso": 84.2
    },
    {
        "identificacion": "2-204-000018",
        "nombre": "Camila",
        "apellido": "Navarro",
        "edad": 30,
        "salario": 690000,
        "ocupacion": "Psicóloga",
        "altura": 1.65,
        "peso": 59.7
    },
    {
        "identificacion": "4-402-000019",
        "nombre": "Javier",
        "apellido": "Ureña",
        "edad": 35,
        "salario": 920000,
        "ocupacion": "Administrador de Redes",
        "altura": 1.76,
        "peso": 80.4
    },
    {
        "identificacion": "5-502-000020",
        "nombre": "Isabel",
        "apellido": "Peña",
        "edad": 47,
        "salario": 1300000,
        "ocupacion": "Empresaria",
        "altura": 1.59,
        "peso": 66.1
    },
    {
        "identificacion": "6-602-000021",
        "nombre": "Andrea",
        "apellido": "Campos",
        "edad": 23,
        "salario": 480000,
        "ocupacion": "Asistente Administrativa",
        "altura": 1.64,
        "peso": 56.8
    },
    {
        "identificacion": "7-702-000022",
        "nombre": "Héctor",
        "apellido": "Valverde",
        "edad": 34,
        "salario": 890000,
        "ocupacion": "Ingeniero Civil",
        "altura": 1.81,
        "peso": 88.9
    },
    {
        "identificacion": "8-802-000023",
        "nombre": "Melissa",
        "apellido": "Aguilar",
        "edad": 28,
        "salario": 610000,
        "ocupacion": "Nutricionista",
        "altura": 1.67,
        "peso": 62.4
    },
    {
        "identificacion": "1-107-000024",
        "nombre": "Ronald",
        "apellido": "Salas",
        "edad": 52,
        "salario": 1650000,
        "ocupacion": "Director",
        "altura": 1.79,
        "peso": 92.0
    },
    {
        "identificacion": "2-205-000025",
        "nombre": "Paola",
        "apellido": "Espinoza",
        "edad": 39,
        "salario": 990000,
        "ocupacion": "Gerente de Proyecto",
        "altura": 1.61,
        "peso": 64.3
    },
    {
        "identificacion": "3-303-000026",
        "nombre": "Alonso",
        "apellido": "Quesada",
        "edad": 25,
        "salario": 540000,
        "ocupacion": "Diseñador Web",
        "altura": 1.72,
        "peso": 70.2
    },
    {
        "identificacion": "4-403-000027",
        "nombre": "Karla",
        "apellido": "Brenes",
        "edad": 44,
        "salario": 1250000,
        "ocupacion": "Médica",
        "altura": 1.57,
        "peso": 60.9
    },
    {
        "identificacion": "5-503-000028",
        "nombre": "Mauricio",
        "apellido": "Sánchez",
        "edad": 37,
        "salario": 950000,
        "ocupacion": "Supervisor",
        "altura": 1.83,
        "peso": 91.1
    },
    {
        "identificacion": "9-902-000029",
        "nombre": "Diana",
        "apellido": "Leiva",
        "edad": 20,
        "salario": 390000,
        "ocupacion": "Cajera",
        "altura": 1.54,
        "peso": 50.3
    },
    {
        "identificacion": "1-108-000030",
        "nombre": "Tomás",
        "apellido": "Araya",
        "edad": 46,
        "salario": 1400000,
        "ocupacion": "Consultor",
        "altura": 1.74,
        "peso": 83.7
    }
]

# PROGRAMA (MENU, SALARIO, Y OTROS DATOS DE LAS PERSONAS)

def mostrar_menu():
    print("-" * 87)
    print(" MENÚ: ")
    print("-" * 87)
    print("1. Agregar nueva persona")
    print("2. Imprimir todas las personas")
    print("3. Persona con mayor IMC")
    print("4. Media del salario")
    print("5. Varianza del salario")
    print("6. Media de la altura")
    print("7. Persona más alta")
    print("8. Persona con el mayor peso")
    print("9. Salir del sistema")


def agregar_persona(personas):
    persona = {
        "identificacion": input("Ingrese la cédula: "),
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "edad": int(input("Edad: ")),
        "salario": float(input("Salario: ")),
        "ocupacion": input("Ocupación: "),
        "altura": float(input("Altura: ")),
        "peso": float(input("Peso: "))
    }
    personas.append(persona)
    print("SE AGREGÓ A LA PERSONA. ")


def imprimir_personas(personas):
    for p in personas:
        print(p)

def persona_mayor_imc(personas):
    mayor = None
    mayor_imc = 0

    for p in personas:
        imc = p["peso"] / (p["altura"] ** 2)
        if imc > mayor_imc:
            mayor_imc = imc
            mayor = p

    print("PERSONA CON MAYOR IMC: ")
    print(mayor)
    print("IMC:", round(mayor_imc, 2))


def media_salario(personas):
    suma = 0
    for p in personas:
        suma += p["salario"]

    media = suma / len(personas)
    print("MEDIA DEL SALARIO: ", media)


def varianza_salario(personas):
    n = len(personas)
    suma = 0

    for p in personas:
        suma += p["salario"]

    media = suma / n

    suma_varianza = 0
    for p in personas:
        suma_varianza += (p["salario"] - media) ** 2

    varianza = suma_varianza / (n - 1)
    print("VARIANZA DEL SALARIO: ", varianza)


def media_altura(personas):
    suma = 0
    for p in personas:
        suma += p["altura"]

    media = suma / len(personas)
    print("MEDIA DE LA ALTURA: ", media)


def persona_mas_alta(personas):
    mayor = personas[0]
    for p in personas:
        if p["altura"] > mayor["altura"]:
            mayor = p

    print("PERSONA MÁS ALTA: ")
    print(mayor)


def persona_mas_pesada(personas):
    mayor = personas[0]
    for p in personas:
        if p["peso"] > mayor["peso"]:
            mayor = p

    print("PERSONA CON EL MAYOR PESO: ")
    print(mayor)


# Ciclo para qe funcione el menú 

opcion = 0

while opcion != 9:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_persona(personas)
    elif opcion == 2:
        imprimir_personas(personas)
    elif opcion == 3:
        persona_mayor_imc(personas)
    elif opcion == 4:
        media_salario(personas)
    elif opcion == 5:
        varianza_salario(personas)
    elif opcion == 6:
        media_altura(personas)
    elif opcion == 7:
        persona_mas_alta(personas)
    elif opcion == 8:
        persona_mas_pesada(personas)
    elif opcion == 9:
        print("Saliendo...")
        break
    else:
        print("Esa opción no existe, ingrese otra opción disponible.")
        continue


# Agregué esto (linea 454 a 474) porque tenía problemas cuando corría el programa
# ya que se ejecutaba el menú
# cada vez que el usuario ponía algo de inmediato, 
# entonces decidí ponerle esta parte para que 
# el menú solo se ejecute al inicio 
# y que la consola 
# pregunte si se desea realizar otra consulta o salir del programa.
# para evitar enredos en la consola.

    if opcion >= 1 and opcion <= 8:
        print("-------¿Desea realizar otra consulta de la lista?------")
        print("1. Sí")
        print("2. No")
        continuar = int(input("Seleccione una opción: "))

        if continuar == 1:
            print("Redirigiendo al menú...")
        elif continuar == 2:
            print("Saliendo del programa...")
            break
        else:
            while continuar != 1 and continuar != 2:
                print("Esa opcion no existe, por favor intente de nuevo con las opciones disponibles")
                continuar = int(input("Seleccione una opción: "))

            if continuar == 1:
                print("Redirigiendo al menú...")
            elif continuar == 2:
                print("Saliendo del programa...")
                break
