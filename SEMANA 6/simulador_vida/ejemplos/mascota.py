class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def __str__(self) -> str:
        return f"Mascota(nombre='{self.nombre}', especie='{self.especie}', edad={self.edad})"