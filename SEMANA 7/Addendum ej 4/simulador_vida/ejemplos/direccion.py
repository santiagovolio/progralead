class Direccion:
    def __init__(self, provincia: str, canton: str, distrito: str):
        self.__provincia = provincia
        self.__canton = canton
        self.__distrito = distrito

    @property
    def provincia(self) -> str:
        return self.__provincia

    @provincia.setter
    def provincia(self, valor: str) -> None:
        self.__provincia = valor

    @property
    def canton(self) -> str:
        return self.__canton

    @canton.setter
    def canton(self, valor: str) -> None:
        self.__canton = valor

    @property
    def distrito(self) -> str:
        return self.__distrito

    @distrito.setter
    def distrito(self, valor: str) -> None:
        self.__distrito = valor

    def __str__(self) -> str:
        return f"{self.__provincia}, {self.__canton}, {self.__distrito}"

    def __len__(self) -> int:
        return len(str(self))