class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int, tipo: str):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = tipo

    def __str__(self) -> str:
        return f"Vehiculo(marca='{self.marca}', modelo='{self.modelo}', anio={self.anio}, tipo='{self.tipo}')"