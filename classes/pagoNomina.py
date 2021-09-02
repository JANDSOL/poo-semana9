class PagoNomina:
    __auto_incrementoId = 0
    def __init__(self, fec='', com=0, ies=0, ant=0, pre='', emp='', sobTie='') -> None:
        self.__id = PagoNomina.__auto_incrementoId
        self.fecha = fec
        self.comision = com
        self.antiguedad = ant
        self.prestamo = pre
        self.empleado = emp
        self.__sueldo = self.empleado.sueldo
        self.iess = self.__calculo_iess(ies, self.__sueldo)
        self.__total_ingreso = self.__total_ingreso(self.__sueldo, self.antiguedad)
        self.__total_descuento = self.__total_descuento(self.comision, self.iess, self.prestamo.cuota)
        self.__liquido_recibir = self.__calculo_liquido(self.__total_ingreso, self.__total_descuento)
        self.sobretiempo = sobTie
        PagoNomina.__auto_incrementoId += 1

    def __calculo_iess(self, iess, sueldo) -> float:
        return round((iess * sueldo), 2)
    
    def __total_ingreso(self, sueldo, antiguedad) -> float:
        return round((sueldo + antiguedad), 2)

    def __total_descuento(self, comision, iess, cuota) -> float:
        return round((comision + iess + cuota), 2)
    
    def __calculo_liquido(self, total_ingreso, total_descuento) -> float:
        return round((total_ingreso - total_descuento), 2)

    def mostrar_pago_nomina(self) -> None:
        print('-Clase pagoNomina:')
        print(' id:', self.__id)
        print(' fecha:', self.fecha)
        print(' sueldo:', self.__sueldo)
        print(' comision:', self.comision)
        print(' iess:', self.iess)
        print(' antiguedad:', self.antiguedad)
        print(' total_ingreso:', self.__total_ingreso)
        print(' total_descuento:', self.__total_descuento)
        print(' liquido_recibir:', self.__liquido_recibir)
        print(' Prestamo():', self.prestamo)
        print(' Empleado():', self.empleado)
        print(' Sobretiempo():', self.sobretiempo)
