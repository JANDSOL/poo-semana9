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

    def __str__(self) -> str:
        pagoSobretiempo_cadena = '(' + self.__id + ', ' + self.fecha + ', ' + str(self.horas_recargo) + ', '\
                              + str(self.horas_extraordinarias) + ', ' + str(self.__estado) + ')'
        return pagoSobretiempo_cadena

    def __calcular_estado(self, horas_recargo, horas_extraordinarias) -> bool:
        if horas_recargo != 0 or horas_extraordinarias != 0:
            estado = True
        else:
            estado = False
        return estado

    def mostrar_empleado(self) -> None:
        print('-Clase pagoSobretiempo:')
        print(' id:', self.__id)
        print(' fecha:', self.fecha)
        print(' horas_recargo:', self.horas_recargo)
        print(' horas_extraordinarias:', self.horas_extraordinarias)
        print(' estado:', self.__estado)
        print(' Empleado():', self.empleado)
