from ejemplos.direccion import Direccion

class Persona:
    def __init__(self, nombre: str, edad: int, ocupacion: str, direccion: Direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__ocupacion = ocupacion
        self.__direccion = direccion

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = valor

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__edad = valor

    @property
    def ocupacion(self) -> str:
        return self.__ocupacion

    @ocupacion.setter
    def ocupacion(self, valor: str) -> None:
        self.__ocupacion = valor

    @property
    def direccion(self) -> Direccion:
        return self.__direccion

    @direccion.setter
    def direccion(self, valor: Direccion) -> None:
        self.__direccion = valor

    def __str__(self) -> str:
        return (
            f"Persona(nombre='{self.__nombre}', edad={self.__edad}, "
            f"ocupacion='{self.__ocupacion}', direccion='{self.__direccion}')"
        )

    def __len__(self) -> int:
        return len(self.__nombre)