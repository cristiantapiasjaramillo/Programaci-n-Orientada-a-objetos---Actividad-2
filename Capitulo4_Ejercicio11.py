print("Ingrese número 1:")
num1=int(input())
print("Ingrese número 2:")
num2=int(input())
print("Ingrese número 3:")
num3=int(input())
mayor=0
if num1>num2 and num1>num3:
    mayor=num1
elif num2>num1 and num2>num3:
    mayor=num2
else:
    mayor=num3
print("El mayor valor entre:", num1, ",", num2, "y", num3, "es:", mayor)
