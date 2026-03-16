from animales.pez import Pez


class Tiburon(Pez):
    def __init__(self, nombre, edad, peso, habitat, agua_dulce, dientes):
        super().__init__(nombre, edad, peso, habitat, agua_dulce)
        self.dientes = dientes

    @property
    def dientes(self):
        return self.__dientes

    @dientes.setter
    def dientes(self, valor):
        if valor < 0:
            raise ValueError("La cantidad de dientes no puede ser negativa.")
        self.__dientes = valor

    def __str__(self):
        tipo = "Agua dulce" if self.agua_dulce else "Agua salada"
        return (
            f"Tiburón | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Tipo: {tipo} | "
            f"Dientes: {self.dientes}"
        )