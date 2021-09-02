class Adicion:
    __auto_incrementoId = 0
    def __init__(self, ant=0) -> None:
        self.__id = Adicion.__auto_incrementoId
        self.antiguedad = ant
        Adicion.__auto_incrementoId += 1
