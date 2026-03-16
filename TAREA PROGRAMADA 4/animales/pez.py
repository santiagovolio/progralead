from animales.animal import Animal


class Pez(Animal):
    def __init__(self, nombre, edad, peso, habitat, agua_dulce):
        super().__init__(nombre, edad, peso, habitat)
        self.agua_dulce = agua_dulce

    @property
    def agua_dulce(self):
        return self.__agua_dulce

    @agua_dulce.setter
    def agua_dulce(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("Debe ser True o False.")
        self.__agua_dulce = valor

    def __str__(self):
        tipo = "Agua dulce" if self.agua_dulce else "Agua salada"
        return (
            f"Pez | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Tipo: {tipo}"
        )