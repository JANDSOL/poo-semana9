class Empleado:
    __auto_incrementoId = 0
    def __init__(self, nom='', sue=0, fec_ing='00/00/0000') -> None:
        self.__id = self.__auto_incrementoId
        self.nombre = nom
        self.sueldo = sue
        self.fecha_ingreso = fec_ing
        self.__auto_incrementoId += 1
