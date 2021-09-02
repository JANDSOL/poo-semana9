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
for _ in range(1, 6):
    empl = EmpOficina('Lucas Freidman', 900.40, fecha(2020, 10, 1).strftime('%d/%m/%Y'), True)
    empr = Empresa('Lukas y As.', '0247389763524', '042721089', 'Milagro, vía Kilometro 26.',
                   'Mejorar la calidad de vida en el cantón.', empl, 'Marketing y finanzas.')
    pago_sobr = PagoSobretiempo(fecha(2020, 10, 3).strftime('%d/%m/%Y'), 10.37, 20.63, empl)
    pres = Prestamo(fecha(2020, 10, 15).strftime('%d/%m/%Y'), 300.10, 6, empl)
    dedu = Deduccion(empl.comision)
    adic = Adicion(30.89)
    pago_nomi = PagoNomina(fecha(2020, 10, 15).strftime('%d/%m/%Y'), dedu.comision, dedu.iess, adic.antiguedad, pres, empl, pago_sobr)

    print('')
    empr.mostrar_empresa()
    print('')
    empr.departamento.mostrar_departamento()
    print('')
    empl.mostrar_empleado()
    print('')
    pago_sobr.mostrar_pago_sobretiempo()
    print('')
    pres.mostrar_prestamo()
    print('')
    pago_nomi.mostrar_pago_nomina()
    print('')
