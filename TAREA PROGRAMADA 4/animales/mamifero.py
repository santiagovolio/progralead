from animales.animal import Animal


class Mamifero(Animal):
    def __init__(self, nombre, edad, peso, habitat, dieta):
        super().__init__(nombre, edad, peso, habitat)
        self.dieta = dieta

    @property
    def dieta(self):
        return self.__dieta

    @dieta.setter
    def dieta(self, valor):
        if not valor.strip():
            raise ValueError("La dieta no puede estar vacía.")
        self.__dieta = valor.strip()

    def __str__(self):
        return (
            f"Mamífero | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Dieta: {self.dieta}"
        )