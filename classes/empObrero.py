from .empleado import Empleado


class EmpObrero(Empleado):
    __auto_incrementoId = 0
    def __init__(self, nom='', sue=0, fec_ing=0, sin=False, con_col=False) -> None:
        super().__init__(nom=nom, sue=sue, fec_ing=fec_ing)
        self.__id = EmpObrero.__auto_incrementoId
        self.sindicato = sin
        self.contrato_colectivo = con_col
        EmpObrero.__auto_incrementoId += 1
    
    def mostrar_emp_obrero(self) -> None:
        print('-Clase Empleado Obrero:')
        print(' id:', self.__id)
        print(' sindicato:', self.sindicato)
        print(' contrato_colectivo:', self.contrato_colectivo)
