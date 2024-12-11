print("Ingrese ventas del departamento 1")
ventas_dep1=float(input())
print("Ingrese ventas del departamento 2")
ventas_dep2=float(input())
print("Ingrese ventas del departamento 3")
ventas_dep3=float(input())
print("Ingrese salario de los vendedores")
salario=float(input())
ventas_totales=ventas_dep1+ventas_dep2+ventas_dep3
porcentaje33=ventas_totales*0.33
if ventas_dep1>porcentaje33:
    salario_dep1=salario+0.2*salario
else:
       salario_dep1=salario
if ventas_dep2>porcentaje33:
    salario_dep2=salario+0.2*salario
else:
       salario_dep2=salario
if ventas_dep3>porcentaje33:
    salario_dep3=salario+0.2*salario
else:
       salario_dep3=salario
print("Salario vendedores depto. 1:", salario_dep1, "Salario vendedores depto. 2:", salario_dep2, "Salario vendedores depto. 3:", salario_dep3)
