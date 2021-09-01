class Deduccion:
    __auto_incrementoId = 0
    def __init__(self, com=False) -> None:
        self.__id = self.__auto_incrementoId
        self.comision = self.__verificar_comision(com)
        self.__iess = 0.0945
        self.__auto_incrementoId += 1
