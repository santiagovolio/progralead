from dataclasses import dataclass


@dataclass(frozen=True)
class Palabra:
    original: str
    valor: str


def normalizar_palabra(texto: str) -> str:
    texto = texto.strip().replace(" ", "").upper()

    if not texto:
        raise ValueError("No se permiten palabras vacías.")

    if not texto.isalpha():
        raise ValueError("Solo se permiten letras, no números ni símbolos.")

    return texto


def construir_palabra(texto: str) -> Palabra:
    return Palabra(original=texto, valor=normalizar_palabra(texto))