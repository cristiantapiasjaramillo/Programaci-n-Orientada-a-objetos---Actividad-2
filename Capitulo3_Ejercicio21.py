import math
print("Ingrese lado 1")
lado1=float(input())
print("Ingrese lado 2")
lado2=float(input())
print("Ingrese lado 3")
lado3=float(input())
perimetro=lado1+lado2+lado3
semiperimetro=perimetro/2
area = math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))
print("Perimetro:", perimetro)
print("Semiperimetro:", semiperimetro)
print("Area:", area)
