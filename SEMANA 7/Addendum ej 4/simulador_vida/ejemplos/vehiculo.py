from ejemplos.persona import Persona

class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int, tipo: str, propietario: Persona | None = None):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__tipo = tipo
        self.__propietario = propietario

    @property
    def marca(self) -> str:
        return self.__marca

    @marca.setter
    def marca(self, valor: str) -> None:
        self.__marca = valor

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, valor: str) -> None:
        self.__modelo = valor

    @property
    def anio(self) -> int:
        return self.__anio

    @anio.setter
    def anio(self, valor: int) -> None:
        self.__anio = valor

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, valor: str) -> None:
        self.__tipo = valor

    @property
    def propietario(self) -> Persona | None:
        return self.__propietario

    @propietario.setter
    def propietario(self, valor: Persona | None) -> None:
        self.__propietario = valor

    def __str__(self) -> str:
        if self.__propietario is None:
            dueno = "Sin propietario"
        else:
            dueno = f"Propietario='{self.__propietario.nombre}'"
        return (
            f"Vehiculo(marca='{self.__marca}', modelo='{self.__modelo}', "
            f"anio={self.__anio}, tipo='{self.__tipo}', {dueno})"
        )

    def __len__(self) -> int:
        return len(self.__modelo)