from animales.ave import Ave


class Aguila(Ave):
    def __init__(self, nombre, edad, peso, habitat, puede_volar, envergadura):
        super().__init__(nombre, edad, peso, habitat, puede_volar)
        self.envergadura = envergadura

    @property
    def envergadura(self):
        return self.__envergadura

    @envergadura.setter
    def envergadura(self, valor):
        if valor <= 0:
            raise ValueError("La envergadura debe ser mayor que 0.")
        self.__envergadura = valor

    def __str__(self):
        vuela = "Sí" if self.puede_volar else "No"
        return (
            f"Águila | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Puede volar: {vuela} | "
            f"Envergadura: {self.envergadura} m"
        )