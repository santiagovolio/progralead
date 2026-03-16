class Transporte:
    """
    Clase padre para representar un medio de transporte del zoológico.

    Incluye datos comunes como placa, marca y velocidad máxima.
    """
    def __init__(self, placa, marca, velocidad_maxima):
        self.placa = placa
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        if not valor.strip():
            raise ValueError("La placa no puede estar vacía.")
        self.__placa = valor.strip()

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        if not valor.strip():
            raise ValueError("La marca no puede estar vacía, por favor ingrese una marca.")
        self.__marca = valor.strip()

    @property
    def velocidad_maxima(self):
        return self.__velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self, valor):
        if valor <= 0:
            raise ValueError("La velocidad máxima no puede ser 0.")
        self.__velocidad_maxima = valor

    def __str__(self):
        return (
            f"Transporte | Placa: {self.placa} | Marca: {self.marca} | "
            f"Velocidad máxima: {self.velocidad_maxima} km/h"
        )