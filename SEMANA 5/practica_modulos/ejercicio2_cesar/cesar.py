def encriptar_cesar(texto, n):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    texto = texto.lower()

    for letra in texto:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nuevo_indice = (indice + n) % 26
            resultado += abecedario[nuevo_indice]
        else:
            resultado += letra
    return resultado


def desencriptar_cesar(texto, n):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    texto = texto.lower()

    for letra in texto:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nuevo_indice = (indice - n) % 26
            resultado += abecedario[nuevo_indice]
        else:
            resultado += letra

    return resultado