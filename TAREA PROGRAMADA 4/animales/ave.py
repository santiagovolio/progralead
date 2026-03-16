from animales.animal import Animal


class Ave(Animal):
    def __init__(self, nombre, edad, peso, habitat, puede_volar):
        super().__init__(nombre, edad, peso, habitat)
        self.puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self.__puede_volar

    @puede_volar.setter
    def puede_volar(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("Debe ser True o False.")
        self.__puede_volar = valor

    def __str__(self):
        texto = "Sí" if self.puede_volar else "No"
        return (
            f"Ave | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Puede volar: {texto}"
        )