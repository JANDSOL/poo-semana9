from .empleado import Empleado


class EmpOficina(Empleado):
    __auto_incrementoId = 0
    def __init__(self, nom='', sue=0, fec_ing='00/00/0000', com=False) -> None:
        super().__init__(nom=nom, sue=sue, fec_ing=fec_ing)
        self.__id = self.__auto_incrementoId
        self.comision = com
        self.__auto_incrementoId += 1
