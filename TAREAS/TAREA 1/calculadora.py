def validar_expresion(expresion):
    """
    Valida si la expresión ingresada cumple
    con todas las reglas del enunciado.
    """

    permitidos = "0123456789+-*/ "

    # Verificar que todos los caracteres sean válidos
    for c in expresion:
        if c not in permitidos:
            return False

    # Eliminar espacios al inicio y al final
    expresion = expresion.strip()

    # No permitir expresión vacía
    if expresion == "":
        return False

    # No puede iniciar ni terminar con operador
    if expresion[0] in "+-*/" or expresion[-1] in "+-*/":
        return False

    # No permitir operadores seguidos
    for i in range(len(expresion) - 1):
        if expresion[i] in "+-*/" and expresion[i + 1] in "+-*/":
            return False

    # Separar la expresión en tokens
    tokens = expresion.split()

    # No permitir números negativos
    for token in tokens:
        if token.startswith("-"):
            return False

    # Verificar división entre cero
    for i in range(len(tokens) - 1):
        if tokens[i] == "/" and tokens[i + 1] == "0":
            return False

    return True


def calcular_izquierda_derecha(expresion):
    """
    Calcula la expresión evaluando
    de izquierda a derecha sin prioridad matemática.
    """

    tokens = expresion.split()

    # Tomar el primer número como resultado inicial
    resultado = int(tokens[0])
    i = 1

    while i < len(tokens):
        operador = tokens[i]
        numero = int(tokens[i + 1])

        if operador == "+":
            resultado += numero
        elif operador == "-":
            resultado -= numero
        elif operador == "*":
            resultado *= numero
        elif operador == "/":
            resultado /= numero

        i += 2

    return resultado


def solicitar_expresion():
    """
    Solicita una operación al usuario.
    Permite escribir 'salir' para terminar.
    """
    return input("Ingrese la operación matemática (o 'salir'): ")


def mostrar_resultado(mensaje):
    """Muestra un mensaje en pantalla."""
    print(mensaje)


def main():
    """
    Procedimiento principal del programa.
    """

    print("Calculadora activa. Escriba 'salir' para apagar la calcu.")

    while True:
        expresion = solicitar_expresion()

        # Opción para salir del programa
        if expresion.lower() == "salir":
            print("Calculadora apagada")
            break

        # Validar la expresión
        if not validar_expresion(expresion):
            mostrar_resultado(" Las instrucciones no permiten que el codigo corra este formato")
        else:
            resultado = calcular_izquierda_derecha(expresion)
            mostrar_resultado(f"Resultado: {resultado}\n")


# Ejecutar el programa
main()
