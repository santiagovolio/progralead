from transportes.transporte import Transporte


class Cuadraciclo(Transporte):
    def __init__(self, placa, marca, velocidad_maxima, combustible):
        super().__init__(placa, marca, velocidad_maxima)
        self.combustible = combustible

    @property
    def combustible(self):
        return self.__combustible

    @combustible.setter
    def combustible(self, valor):
        if not valor.strip():
            raise ValueError("El combustible no puede estar vacío.")
        self.__combustible = valor.strip()

    def __str__(self):
        return (
            f"Cuadraciclo | Placa: {self.placa} | Marca: {self.marca} | "
            f"Velocidad máxima: {self.velocidad_maxima} km/h | Combustible: {self.combustible}"
        )