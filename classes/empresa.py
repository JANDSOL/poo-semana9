from .departamento import Departamento


class Empresa:
    __auto_incrementoId = 0
    def __init__(self, nom='', ruc='', tel='', dire='', raz_soc='', emp='', des='') -> None:
        self.__id = self.__auto_incrementoId
        self.nombre = nom
        self.ruc = ruc
        self.telefono = tel
        self.direccion = dire
        self.razon_social = raz_soc
        self.empleado = emp
        self.departamento = Departamento(des, emp)
        self.__auto_incrementoId += 1
