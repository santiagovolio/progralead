from animales.anfibio import Anfibio


class Rana(Anfibio):
    def __init__(self, nombre, edad, peso, habitat, piel_humeda, color):
        super().__init__(nombre, edad, peso, habitat, piel_humeda)
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, valor):
        if not valor.strip():
            raise ValueError("El color no puede estar vacío.")
        self.__color = valor.strip()

    def __str__(self):
        humeda = "Sí" if self.piel_humeda else "No"
        return (
            f"Rana | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Piel húmeda: {humeda} | "
            f"Color: {self.color}"
        )