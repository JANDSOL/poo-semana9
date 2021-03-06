from .departamento import Departamento


class Empresa:
    __auto_incrementoId = 0
    def __init__(self, nom='', ruc='', tel='', dire='', raz_soc='', emp='', des='') -> None:
        self.__id = Empresa.__auto_incrementoId
        self.nombre = nom
        self.ruc = ruc
        self.telefono = tel
        self.direccion = dire
        self.razon_social = raz_soc
        self.empleado = emp
        self.departamento = Departamento(des, emp)
        Empresa.__auto_incrementoId += 1

    def mostrar_empresa(self) -> None:
        print('-Clase Empresa:')
        print(' id:', self.__id)
        print(' nombre:', self.nombre)
        print(' ruc:', self.ruc)
        print(' telefono:', self.telefono)
        print(' direccion:', self.direccion)
        print(' razon_social:', self.razon_social)
        print(' Empleado():', self.empleado)
        print(' Departamento():', self.departamento)
