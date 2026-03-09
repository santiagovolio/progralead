from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Optional, Set
import random
import string

from .palabras import Palabra
from .colores import pintar_color, VERDE_COLOR


Coordenada = Tuple[int, int]
Direccion = Tuple[int, int]


@dataclass
class Colocacion:
    palabra: str
    inicio: Coordenada
    direccion: Direccion
    celdas: List[Coordenada]


class SopaDeLetras:
    def __init__(self, tamano: int = 15) -> None:
        self.tamano = tamano
        self.matriz: List[List[str]] = [["" for _ in range(tamano)] for _ in range(tamano)]
        self.colocaciones: List[Colocacion] = []

        # 8 direcciones (incluye diagonales)
        self.direcciones: List[Direccion] = [
            (0, 1), (0, -1),
            (1, 0), (-1, 0),
            (1, 1), (1, -1),
            (-1, 1), (-1, -1)
        ]

    def generar(self, palabras: List[Palabra]) -> None:
        self.colocaciones.clear()
        self.matriz = [["" for _ in range(self.tamano)] for _ in range(self.tamano)]

        palabras_ordenadas = sorted((p.valor for p in palabras), key=len, reverse=True)

        for palabra in palabras_ordenadas:
            if not self._colocar_palabra(palabra):
                raise RuntimeError(f"No se pudo colocar: {palabra}")

        self._rellenar_aleatorio()

    def renderizar(self, resuelta: bool = False) -> str:
        """
        Devuelve la sopa lista para imprimir.

        Si resuelta=True, colorea las letras de las palabras.
        """
        resaltar: Set[Coordenada] = set()

        if resuelta:
            for c in self.colocaciones:
                resaltar.update(c.celdas)

        lineas: List[str] = []

        for fila in range(self.tamano):
            fila_texto = []
            for col in range(self.tamano):
                letra = self.matriz[fila][col]

                if resuelta and (fila, col) in resaltar:
                    fila_texto.append(pintar_color(letra, VERDE_COLOR))
                else:
                    fila_texto.append(letra)

            lineas.append(" ".join(fila_texto))

        return "\n".join(lineas)

    def resumen_palabras(self) -> str:

        return ", ".join(c.palabra for c in self.colocaciones)


    def _colocar_palabra(self, palabra: str, max_intentos: int = 800) -> bool:
        for _ in range(max_intentos):
            direccion = random.choice(self.direcciones)
            fila = random.randrange(self.tamano)
            col = random.randrange(self.tamano)

            celdas = self._calcular_celdas(palabra, (fila, col), direccion)

            if celdas and self._puede_colocar(palabra, celdas):
                self._aplicar(palabra, celdas, (fila, col), direccion)
                return True

        return False

    def _calcular_celdas(
        self,
        palabra: str,
        inicio: Coordenada,
        direccion: Direccion
    ) -> Optional[List[Coordenada]]:

        fila, col = inicio
        df, dc = direccion
        celdas: List[Coordenada] = []

        for _ in palabra:
            if not (0 <= fila < self.tamano and 0 <= col < self.tamano):
                return None
            celdas.append((fila, col))
            fila += df
            col += dc

        return celdas

    def _puede_colocar(self, palabra: str, celdas: List[Coordenada]) -> bool:
        for i, (f, c) in enumerate(celdas):
            existente = self.matriz[f][c]
            requerida = palabra[i]
            if existente != "" and existente != requerida:
                return False
        return True

    def _aplicar(
        self,
        palabra: str,
        celdas: List[Coordenada],
        inicio: Coordenada,
        direccion: Direccion
    ) -> None:

        for i, (f, c) in enumerate(celdas):
            self.matriz[f][c] = palabra[i]

        self.colocaciones.append(
            Colocacion(palabra, inicio, direccion, celdas)
        )

    def _rellenar_aleatorio(self) -> None:
        for f in range(self.tamano):
            for c in range(self.tamano):
                if self.matriz[f][c] == "":
                    self.matriz[f][c] = random.choice(string.ascii_uppercase)