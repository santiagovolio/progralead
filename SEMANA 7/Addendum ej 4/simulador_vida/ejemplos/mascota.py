class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = valor

    @property
    def especie(self) -> str:
        return self.__especie

    @especie.setter
    def especie(self, valor: str) -> None:
        self.__especie = valor

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__edad = valor

    def __str__(self) -> str:
        return f"Mascota(nombre='{self.__nombre}', especie='{self.__especie}', edad={self.__edad})"

    def __len__(self) -> int:
        return len(self.__nombre)