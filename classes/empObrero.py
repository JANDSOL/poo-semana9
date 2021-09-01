from .empleado import Empleado


class EmpObrero(Empleado):
    __auto_incrementoId = 0
    def __init__(self, nom='', sue=0, fec_ing='00/00/0000', sin=False, con_col=False) -> None:
        super().__init__(nom=nom, sue=sue, fec_ing=fec_ing)
        self.__id = self.__auto_incrementoId
        self.sindicato = sin
        self.contrato_colectivo = con_col
        self.__auto_incrementoId += 1
