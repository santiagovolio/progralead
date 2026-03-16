from empleados.empleado import Empleado


class Veterinario(Empleado):
    def __init__(self, identificacion, nombre, edad, salario, especialidad):
        super().__init__(identificacion, nombre, edad, salario)
        self.especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not valor.strip():
            raise ValueError("La especialidad no puede estar vacía.")
        self.__especialidad = valor.strip()

    def __str__(self):
        return (
            f"Veterinario | Cédula: {self.identificacion} | Nombre: {self.nombre} | "
            f"Edad: {self.edad} | Salario: {self.salario:.2f} | Especialidad: {self.especialidad}"
        )