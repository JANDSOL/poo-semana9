class Adicion:
    __auto_incrementoId = 0
    def __init__(self, com=0, ant=0) -> None:
        self.__id = Adicion.__auto_incrementoId
        self.comision = self.__verificar_comision(com)
        self.antiguedad = self.__calculo_antiguedad(ant)
        Adicion.__auto_incrementoId += 1

    def __verificar_comision(self, comision) -> float:
        if comision is True:
            calcular_com = round((float(input('Ingresa la comision: %'))) / 100, 4)
        else:
            calcular_com = 0
        return calcular_com

    def __calculo_antiguedad(self, antiguedad) -> float:
        return round((antiguedad / 100), 4)
