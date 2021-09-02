class Deduccion:
    __auto_incrementoId = 0
    def __init__(self, com=False) -> None:
        self.__id = Deduccion.__auto_incrementoId
        self.comision = self.__verificar_comision(com)
        self.__iess = 0.0945
        Deduccion.__auto_incrementoId += 1
    
    def __verificar_comision(self, comision) -> float:
        if comision is True:
            calcular_com = float(input('Ingresa la comision: '))
        else:
            calcular_com = 0
        return calcular_com

    @property
    def iess(self):
        return self.__iess

    @iess.setter
    def iess(self, ies=0.0945):
        self.__iess = ies
