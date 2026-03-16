from animales.reptil import Reptil


class Cocodrilo(Reptil):
    def __init__(self, nombre, edad, peso, habitat, es_venenoso, largo):
        super().__init__(nombre, edad, peso, habitat, es_venenoso)
        self.largo = largo

    @property
    def largo(self):
        return self.__largo

    @largo.setter
    def largo(self, valor):
        if valor <= 0:
            raise ValueError("El largo debe ser mayor que 0.")
        self.__largo = valor

    def __str__(self):
        venenoso = "Sí" if self.es_venenoso else "No"
        return (
            f"Cocodrilo | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Venenoso: {venenoso} | "
            f"Largo: {self.largo} m"
        )