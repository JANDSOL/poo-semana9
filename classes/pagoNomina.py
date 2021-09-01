class PagoNomina:
    __auto_incrementoId = 0
    def __init__(self, fec='', sue=0, com=0, ies=0, ant=0, pre='', emp='', sobTie='') -> None:
        self.__id = self.__auto_incrementoId
        self.fecha = fec
        self.sueldo = sue
        self.comision = com
        self.iess = self.__calculo_iess(ies, self.sueldo)
        self.antiguedad = ant
        self.prestamo = pre
        self.__total_ingreso = self.__total_ingreso(self.sueldo, self.antiguedad)
        self.__total_descuento = self.__total_descuento(self.comision, self.iess, self.prestamo.valor)
        self.__liquido_recibir = self.__calculo_liquido(self.__total_ingreso, self.__total_descuento)
        self.empleado = emp
        self.sobretiempo = sobTie
        self.__auto_incrementoId += 1
