from sopa.sopa_letras import SopaDeLetras
from sopa.palabras import construir_palabra


MAXIMO_PALABRAS = 15
TAMANO_SOPA = 35


def _separar_entrada(entrada: str) -> list[str]:
    partes = entrada.split(",")
    return [p.strip() for p in partes if p.strip()]


def ingresar_palabras() -> list[str]:
    while True:
        entrada = input(
            "Ingrese hasta 15 palabras para generar la sopa "
            "(separadas por coma) y presione ENTER: "
        ).strip()

        # Si está vacío → volver a pedir
        if not entrada:
            print("Debe ingresar al menos una palabra válida.\n")
            continue

        candidatos = _separar_entrada(entrada)[:MAXIMO_PALABRAS]

        palabras_validas = []
        palabras_invalidas = []

        for texto in candidatos:
            try:
                palabras_validas.append(construir_palabra(texto).valor)
            except ValueError:
                palabras_invalidas.append(texto)

        # Palabras inválidas 
        if palabras_invalidas:
            print("Se omitieron por inválidas:", ", ".join(palabras_invalidas))

        # Pedir q las vuelva a poner si no hay ninguna válida
        if not palabras_validas:
            print("Debe ingresar al menos una palabra válida.\n")
            continue

        return palabras_validas

def main() -> None:
    lista_palabras = ingresar_palabras()

    print("\nGenerando Sopa..\n")
    print(" ")
    print(" ")

    sopa = SopaDeLetras(tamano=TAMANO_SOPA)
    sopa.generar([construir_palabra(p) for p in lista_palabras])

    print("=== SOPA DE LETRAS ===\n")
    print(" ")
    print(sopa.renderizar(resuelta=False))

    print(" ")
    print("\nPalabras a encontrar:")
    print(" ")
    print(sopa.resumen_palabras())
    print(" ")
    opcion = input("\nPresione 'R' para mostrar la solución o cualquier tecla para salir: ").strip().upper()
    print(" ")
    if opcion == "R":
        print("\n=== SOPA RESUELTA ===\n")
        print(sopa.renderizar(resuelta=True))
    print(" ")

if __name__ == "__main__":
    main()