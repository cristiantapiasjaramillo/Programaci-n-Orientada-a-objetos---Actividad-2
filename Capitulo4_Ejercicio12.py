print("Ingrese nombre:")
nombre=str(input())
print("Ingrese número de horas trabajadas:")
horas_trabajadas=int(input())
print("Ingrese valor por hora de trabajo:")
pago_hora=float(input())
if horas_trabajadas>40:
    horas_extras=horas_trabajadas-40
    if horas_extras>8:
      horas_extras_mayor_8=horas_extras-8
      salario=40*pago_hora+16*pago_hora+horas_extras_mayor_8*3*pago_hora
    elif horas_extras<=8:
      pago_horas_extras=pago_hora*2*horas_extras
      salario=pago_hora*40+pago_horas_extras
else:
    salario=pago_hora*horas_trabajadas
print("El trabajador", nombre, "devengó: $", salario)
