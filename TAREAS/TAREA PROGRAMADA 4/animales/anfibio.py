from animales.animal import Animal


class Anfibio(Animal):
    def __init__(self, nombre, edad, peso, habitat, piel_humeda):
        super().__init__(nombre, edad, peso, habitat)
        self.piel_humeda = piel_humeda

    @property
    def piel_humeda(self):
        return self.__piel_humeda

    @piel_humeda.setter
    def piel_humeda(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("Debe ser True o False.")
        self.__piel_humeda = valor

    def __str__(self):
        texto = "Sí" if self.piel_humeda else "No"
        return (
            f"Anfibio | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Piel húmeda: {texto}"
        )