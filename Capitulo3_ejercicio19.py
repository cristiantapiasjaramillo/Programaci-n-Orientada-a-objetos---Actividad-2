import math
print("Ingrese la medida del lado")
lado=float(input())
perimetro_triangulo=3*lado
altura_triangulo=((math.sqrt(3)*lado)/2)
area_triangulo=lado*altura_triangulo
print("El preimetro del triangulo es:", perimetro_triangulo)
print("la altura del triangulo es:", altura_triangulo)
print("El area del triangulo es:", area_triangulo)
