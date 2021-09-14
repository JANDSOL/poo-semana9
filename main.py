from datetime import date as fecha
from classes.empOficina import EmpOficina
from classes.empObrero import EmpObrero
from classes.empresa import Empresa
from classes.prestamo import Prestamo
from classes.pagoSobretiempo import PagoSobretiempo
from classes.adicion import Adicion
from classes.deduccion import Deduccion
from classes.pagoNomina import PagoNomina


#TODO: IMPLEMENTAR INGRESO DE DATOS PARA TODAS LAS CLASES.
empl = EmpOficina('Lucas Freidman', 900.40, fecha(2020, 10, 1), True)
# empl = EmpObrero('Lucas Freidman', 900.40, fecha(2020, 10, 1), True, True)
empr = Empresa('Lukas y As.', '0247389763524', '042721089', 'Milagro, vía Kilometro 26.',
               'Mejorar la calidad de vida en el cantón.', empl, 'Recursos Humanos.')
pago_sobr = PagoSobretiempo(fecha(2020, 10, 1), 4, 2, empl)
pres = Prestamo(fecha(2020, 10, 15), 300.10, 6, empl)
# pres = Prestamo(emp=empl)
if isinstance(empl, EmpOficina):
    adic = Adicion(com=empl.comision)
else:  # Obrero solo tiene adicion de antiguedad
    adic = Adicion(ant=30.89)
dedu = Deduccion()
dedu.iess = 9.45
pago_nomi = PagoNomina(fecha(2020, 10, 31), adic.comision, dedu.iess, adic.antiguedad, pres, empl, pago_sobr)

print('')
empr.mostrar_empresa()
print('')
empr.departamento.mostrar_departamento()
print('')
empl.mostrar_empleado()
print('')
if isinstance(empl, EmpOficina):
    empl.mostrar_emp_oficina()
else:
    empl.mostrar_emp_obrero()
print('')
pago_sobr.mostrar_pago_sobretiempo()
print('')
pres.mostrar_prestamo()
print('')
print('')
pago_nomi.mostrar_pago_nomina()
print('')
