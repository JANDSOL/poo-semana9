class Deduccion:
    __auto_incrementoId = 0
    def __init__(self) -> None:
        self.__id = Deduccion.__auto_incrementoId
        self.__iess = 0
        Deduccion.__auto_incrementoId += 1

    @property
    def iess(self) -> float:
        return self.__iess

    @iess.setter
    def iess(self, ies=0) -> None:
        self.__iess = round((ies / 100), 4)
