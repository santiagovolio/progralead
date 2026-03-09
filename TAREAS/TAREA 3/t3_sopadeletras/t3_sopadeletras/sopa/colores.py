# Colores para la consola: se llaman ANSI, según lo que investigué en google 


REINICIAR_COLOR = "\033[0m"
VERDE_COLOR = "\033[32m"


def pintar_color(texto: str, codigo_color: str) -> str:
    return f"{codigo_color}{texto}{REINICIAR_COLOR}"

def demo_colores_bruto() -> None:

    import random
    import string

    letra = random.choice(string.ascii_lowercase)
    print("[VERDE]", letra)
    print(letra)

    letra = random.choice(string.ascii_lowercase)
    print(pintar_color(letra, VERDE_COLOR))
