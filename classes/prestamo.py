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

    def __str__(self) -> str:
        prestamo_cadena = '(' + self.__id + ', ' + self.fecha + ', ' + str(self.valor) + ', ' + str(self.numero_pagos)\
                              + ', ' + str(self.cuota) + ', ' + str(self.__saldo) + ', ' + str(self.__estado) + ')'
        return prestamo_cadena
    
    def __calcular_saldo(self, valor, numero_pagos, cuota) -> float:
        if numero_pagos != 0:
            saldo = round(((numero_pagos * cuota) - valor), 2)
        else:
            saldo = round((cuota - valor), 2)
        return saldo

    def __calcular_estado(self, saldo) -> bool:
        if saldo != 0:
            estado = True
        else:
            estado = False
        return estado

    def mostrar_empleado(self) -> None:
        print('-Clase Prestamo:')
        print(' id:', self.__id)
        print(' fecha:', self.fecha)
        print(' valor:', self.valor)
        print(' numero_pagos:', self.numero_pagos)
        print(' cuota:', self.cuota)
        print(' saldo:', self.__saldo)
        print(' estado:', self.__estado)
        print(' Empleado():', self.empleado)
