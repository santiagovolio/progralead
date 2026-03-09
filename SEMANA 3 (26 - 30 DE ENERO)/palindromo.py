def limpiar_texto(texto):
    texto_corriente = ""

    for caracter in texto.lower():
        if caracter.isalnum():  # Solo letras y números
            texto_corriente += caracter

    return texto_corriente


def es_palindromo(texto):
    texto_corriente = limpiar_texto(texto)
    texto_invertido = texto_corriente[::-1]

    return texto_corriente == texto_invertido

def main():
    texto = input("Ingrese una palabra o frase: ")

    if es_palindromo(texto):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")


# Ejecutar el programa
main()
