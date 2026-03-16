from empleados.empleado import Empleado


class Conserje(Empleado):
    def __init__(self, identificacion, nombre, edad, salario, turno):
        super().__init__(identificacion, nombre, edad, salario)
        self.turno = turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, valor):
        if not valor.strip():
            raise ValueError("El turno no puede estar vacío.")
        self.__turno = valor.strip()

    def __str__(self):
        return (
            f"Conserje | Cédula: {self.identificacion} | Nombre: {self.nombre} | "
            f"Edad: {self.edad} | Salario: {self.salario:.2f} | Turno: {self.turno}"
        )