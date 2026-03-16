from animales.mamifero import Mamifero


class Leon(Mamifero):
    def __init__(self, nombre, edad, peso, habitat, dieta, melena):
        super().__init__(nombre, edad, peso, habitat, dieta)
        self.melena = melena

    @property
    def melena(self):
        return self.__melena

    @melena.setter
    def melena(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("Debe ser True o False.")
        self.__melena = valor

    def __str__(self):
        texto = "Sí" if self.melena else "No"
        return (
            f"León | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Dieta: {self.dieta} | "
            f"Tiene melena: {texto}"
        )