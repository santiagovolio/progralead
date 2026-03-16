class Animal:
    """
    Clase padre para representar un animal del zoológico.
    Contiene información general como nombre, edad, peso y hábitat.
    """

    def __init__(self, nombre, edad, peso, habitat):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.habitat = habitat

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__edad = valor

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        if valor <= 0:
            raise ValueError("El peso debe ser mayor que 0.")
        self.__peso = valor

    @property
    def habitat(self):
        return self.__habitat

    @habitat.setter
    def habitat(self, valor):
        if not valor.strip():
            raise ValueError("El hábitat no puede estar vacío.")
        self.__habitat = valor.strip()

    def __str__(self):
        return (
            f"Animal | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat}"
        )