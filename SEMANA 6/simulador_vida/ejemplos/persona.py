class Persona:
    def __init__(self, nombre: str, edad: int, ocupacion: str):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def __str__(self) -> str:
        return f"Persona(nombre='{self.nombre}', edad={self.edad}, ocupacion='{self.ocupacion}')"