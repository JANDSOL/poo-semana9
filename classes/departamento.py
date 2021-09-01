class Departamento:
    __auto_incrementoId = 0
    def __init__(self, des='', emp='') -> None:
        self.__id = self.__auto_incrementoId
        self.descripcion = des
        self.empleado = emp
        self.__auto_incrementoId += 1
