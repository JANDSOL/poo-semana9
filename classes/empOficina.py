from .empleado import Empleado


class EmpOficina(Empleado):
    __auto_incrementoId = 0
    def __init__(self, nom='', sue=0, fec_ing='00/00/0000', com=False) -> None:
        super().__init__(nom=nom, sue=sue, fec_ing=fec_ing)
        self.__id = EmpOficina.__auto_incrementoId
        self.comision = com
        EmpOficina.__auto_incrementoId += 1
    
    def mostrar_emp_oficina(self) -> None:
        print('-Clase Empleado Oficina:')
        print(' id:', self.__id)
        print(' comision:', self.comision)
