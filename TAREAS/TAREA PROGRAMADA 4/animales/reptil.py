from animales.animal import Animal


class Reptil(Animal):
    def __init__(self, nombre, edad, peso, habitat, es_venenoso):
        super().__init__(nombre, edad, peso, habitat)
        self.es_venenoso = es_venenoso

    @property
    def es_venenoso(self):
        return self.__es_venenoso

    @es_venenoso.setter
    def es_venenoso(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("Debe ser True o False.")
        self.__es_venenoso = valor

    def __str__(self):
        texto = "Sí" if self.es_venenoso else "No"
        return (
            f"Reptil | Nombre: {self.nombre} | Edad: {self.edad} años | "
            f"Peso: {self.peso} kg | Hábitat: {self.habitat} | Venenoso: {texto}"
        )