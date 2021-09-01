class Departamento:
    __auto_incrementoId = 0
    def __init__(self, des='', emp='') -> None:
        self.__id = self.__auto_incrementoId
        self.descripcion = des
        self.empleado = emp
        self.__auto_incrementoId += 1

    def __str__(self) -> str:
        departamento_cadena = '(' + self.__id + ', ' + self.descripcion + ')'
        return departamento_cadena

    def mostrar_departamento(self) -> None:
        print('-Clase Departamento:')
        print(' id:', self.__id)
        print(' descripcion:', self.descripcion)
        print(' Empleado():', self.empleado)
