from empleados.empleado import Empleado


class Guardian(Empleado):
    def __init__(self, identificacion, nombre, edad, salario, zona):
        super().__init__(identificacion, nombre, edad, salario)
        self.zona = zona

    @property
    def zona(self):
        return self.__zona

    @zona.setter
    def zona(self, valor):
        if not valor.strip():
            raise ValueError("La zona no puede estar vacía.")
        self.__zona = valor.strip()

    def __str__(self):
        return (
            f"Guardián | Cédula: {self.identificacion} | Nombre: {self.nombre} | "
            f"Edad: {self.edad} | Salario: {self.salario:.2f} | Zona: {self.zona}"
        )