from empleados.empleado import Empleado


class Administrador(Empleado):
    def __init__(self, identificacion, nombre, edad, salario, area):
        super().__init__(identificacion, nombre, edad, salario)
        self.area = area

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, valor):
        if not valor.strip():
            raise ValueError("El área no puede estar vacía.")
        self.__area = valor.strip()

    def __str__(self):
        return (
            f"Administrador | Cédula: {self.identificacion} | Nombre: {self.nombre} | "
            f"Edad: {self.edad} | Salario: {self.salario:.2f} | Área: {self.area}"
        )