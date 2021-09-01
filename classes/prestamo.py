class Prestamo:
    __auto_incrementoId = 0
    def __init__(self, fec='', valo=0, num_pag=0, cuo=0, emp='') -> None:
        self.__id = self.__auto_incrementoId
        self.fecha = fec
        self.valor = valo
        self.numero_pagos = num_pag
        self.cuota = cuo
        self.__saldo = self.__calcular_saldo(self.valor, self.numero_pagos, self.cuota)
        self.__estado = self.__calcular_estado(self.__saldo)
        self.empleado = emp
        self.__auto_incrementoId += 1
