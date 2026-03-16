from transportes.transporte import Transporte


class Patineta(Transporte):
    def __init__(self, placa, marca, velocidad_maxima, electrica):
        super().__init__(placa, marca, velocidad_maxima)
        self.electrica = electrica

    @property
    def electrica(self):
        return self.__electrica

    @electrica.setter
    def electrica(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El valor de eléctrica debe ser True o False.")
        self.__electrica = valor

    def __str__(self):
        tipo = "Eléctrica" if self.electrica else "Manual"
        return (
            f"Patineta | Placa: {self.placa} | Marca: {self.marca} | "
            f"Velocidad máxima: {self.velocidad_maxima} km/h | Tipo: {tipo}"
        )