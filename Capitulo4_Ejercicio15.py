print("Ingrese peso de la esfera A")
pesoA=float(input())
print("Ingrese peso de la esfera B")
pesoB=float(input())
print("Ingrese peso de la esfera C")
pesoC=float(input())
print("Ingrese peso de la esfera D")
pesoD=float(input())
if pesoA==pesoB and pesoA==pesoC:
    if pesoD>pesoA:
        print("La esfera D es la diferente y es de mayor peso")
    elif pesoD<pesoA:
        print("La esfera D es la diferente y es de menor peso")
if pesoA==pesoB and pesoA==pesoD:
    if pesoC>pesoA:
        print("La esfera C es la diferente y es de mayor peso")
    elif pesoC<pesoA:
        print("La esfera C es la diferente y es de menor peso")
if pesoA==pesoC and pesoA==pesoD:
    if pesoB>pesoD:
        print("La esfera B es la diferente y es de mayor peso")
    elif pesoB<pesoD:
        print("La esfera B es la diferente y es de menor peso")
else:
    if pesoA>pesoB:
        print("La esfera A es la diferente y es de mayor peso")
    elif pesoA<pesoB:
        print("La esfera A es la diferente y es de menor peso")
