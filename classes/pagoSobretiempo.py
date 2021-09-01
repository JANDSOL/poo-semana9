class PagoSobretiempo:
    __auto_incrementoId = 0
    def __init__(self, fec='', hor_rec=0, hor_ext=0, emp='') -> None:
        self.__id = self.__auto_incrementoId
        self.fecha = fec
        self.horas_recargo = hor_rec
        self.horas_extraordinarias = hor_ext
        self.__estado = self.__calcular_estado(self.horas_recargo, self.horas_extraordinarias)
        self.empleado = emp
        self.__auto_incrementoId += 1
