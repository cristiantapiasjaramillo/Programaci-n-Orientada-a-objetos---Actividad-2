import math
print("Ingrese parametro A")
a=float(input())
print("Ingrese parametro B")
b=float(input())
print("Ingrese parametro C")
c=float(input())
discriminante = b**2 - 4*a*c
if discriminante > 0:
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("x1:", x1, "x2:", x2)
elif discriminante == 0:
        x = -b / (2 * a)
        print("x:", x)
else:
    print("La ecuación no tiene soluciones reales.")
