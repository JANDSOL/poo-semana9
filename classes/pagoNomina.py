class PagoNomina:
    __auto_incrementoId = 0
    def __init__(self, fec=0, com=0, ies=0, ant=0, pre='', emp='', sobTie='') -> None:
        self.__id = PagoNomina.__auto_incrementoId
        self.fecha = fec
        self.prestamo = pre
        self.empleado = emp
        self.__sueldo = self.empleado.sueldo
        self.antiguedad = self.__calculo_antiguedad(ant, self.fecha, self.empleado.fecha_ingreso, self.__sueldo)
        self.comision = self.__calculo_comision(com, self.__sueldo)
        self.iess = self.__calculo_iess(ies, self.__sueldo)
        self.sobretiempo = sobTie
        self.calcular_sobretiempo = self.sobretiempo.calcular_sobretiempo(self.__sueldo)
        self.cuotaPrestamo = self.prestamo.cuota
        self.__total_ingreso = self.__total_ingreso(self.__sueldo, self.calcular_sobretiempo, self.comision, self.antiguedad)
        self.__total_descuento = self.__total_descuento(self.iess, self.prestamo.cuota)
        self.__liquido_recibir = self.__calculo_liquido(self.__total_ingreso, self.__total_descuento)
        PagoNomina.__auto_incrementoId += 1

    def __calculo_antiguedad(self, ant, f_n, f_i, sue) -> float:
        fechas = ((f_n - f_i).days) + 1
        return round((ant * fechas / 365 * sue), 2)

    def __calculo_comision(self, comision, sueldo) -> float:
        return round((comision * sueldo))

    def __calculo_iess(self, iess, sueldo) -> float:
        return round((iess * sueldo), 2)
    
    def __total_ingreso(self, sueldo, sobretiempo, comision, antiguedad) -> float:
        return round((sueldo + sobretiempo + comision + antiguedad), 2)

    def __total_descuento(self, iess, cuota) -> float:
        return round((iess + cuota), 2)
    
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
        print(' Calculo Sobretiempo:', self.calcular_sobretiempo)
        print(' Cuota Prestamo:', self.cuotaPrestamo)
