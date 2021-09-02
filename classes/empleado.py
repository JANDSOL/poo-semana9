class Empleado:
    __auto_incrementoId = 0
    def __init__(self, nom='', sue=0, fec_ing='00/00/0000') -> None:
        self.__id = self.__auto_incrementoId
        self.nombre = nom
        self.sueldo = sue
        self.fecha_ingreso = fec_ing
        self.__auto_incrementoId += 1

    def __str__(self) -> str:
        empleado_cadena = '(' + str(self.__id) + ', ' + self.nombre + ', ' + str(self.sueldo) + ', ' + self.fecha_ingreso + ')'
        return empleado_cadena

    def mostrar_empleado(self) -> None:
        print('-Clase Empleado:')
        print(' id:', self.__id)
        print(' nombre:', self.nom)
        print(' sueldo:', self.sueldo)
        print(' fecha_ingreso:', self.fecha_ingreso)
