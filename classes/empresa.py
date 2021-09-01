from .empleado import Empleado
from .departamento import Departamento


class Empresa:
    __auto_incrementoId = 0
    def __init__(self, nom='', ruc='', tel='', dire='', raz_soc='', emEmpl_nom='', sue=0, fec_ing='', des='', emp='') -> None:
        self.__id = self.__auto_incrementoId
        self.nombre = nom
        self.ruc = ruc
        self.telefono = tel
        self.direccion = dire
        self.razon_social = raz_soc
        self.empleado = Empleado(emEmpl_nom, sue, fec_ing)
        self.__departamento = Departamento(des, emp)
        self.__auto_incrementoId += 1
