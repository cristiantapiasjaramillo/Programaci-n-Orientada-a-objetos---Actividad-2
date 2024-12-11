print("Ingrese el peso de la esfera A")
pesoA=float(input())
print("Ingrese el peso de la esfera B")
pesoB=float(input())
print("Ingrese el peso de la esfera C")
pesoC=float(input())
if pesoA>pesoB and pesoA>pesoC:
    print("La esfera A es la de mayor peso")
elif pesoB>pesoA and pesoB>pesoC:
    print("La esfera B es la de mayor peso")
else:
    print("La esfera C es la de mayor peso")
