print("Ingrese nombre")
nombre=str(input())
print("Ingrese el salario por hora")
salario_hora=float(input())
print("Ingrese las horas trabajadas en el mes")
horas_trabajadas_mes=int(input())
salario_mensual=salario_hora*horas_trabajadas_mes
if salario_mensual>450000:
    print(nombre, salario_mensual)
else:
    print(nombre)
