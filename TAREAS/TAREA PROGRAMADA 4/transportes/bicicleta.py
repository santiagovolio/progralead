from transportes.transporte import Transporte


class Bicicleta(Transporte):
    def __init__(self, placa, marca, velocidad_maxima, tipo):
        super().__init__(placa, marca, velocidad_maxima)
        self.tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        if not valor.strip():
            raise ValueError("El tipo no puede estar vacío.")
        self.__tipo = valor.strip()

    def __str__(self):
        return (
            f"Bicicleta | Placa: {self.placa} | Marca: {self.marca} | "
            f"Velocidad máxima: {self.velocidad_maxima} km/h | Tipo: {self.tipo}"
        )