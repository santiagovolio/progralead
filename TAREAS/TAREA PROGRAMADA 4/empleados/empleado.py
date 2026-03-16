class Empleado:
    """
    Clase padre para representar un empleado del zoológico.

    Maneja información general como la cédula, nombre, edad, y el salario del empleado.
    """

    def __init__(self, identificacion, nombre, edad, salario):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not valor.strip():
            raise ValueError("La cédula no puede estar vacía")
        self.__identificacion = valor.strip()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor <= 0:
            raise ValueError("La edad debe ser mayor que 0.")
        self.__edad = valor

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__salario = valor

    def __str__(self):
        return (
            f"Empleado | Cédula: {self.identificacion} | Nombre: {self.nombre} | "
            f"Edad: {self.edad} | Salario: {self.salario:.2f}"
        )