print("Ingrese el valor de la compra:")
valor_compra=float(input())
print("Ingrese el color de la bola:")
color=str(input())
if color=="blanco":
    porcentaje_descuento=0
elif color=="verde":
     porcentaje_descuento=10
elif color=="amarillo":
        porcentaje_descuento=25
elif color=="azul":
         porcentaje_descuento=50
else:
         porcentaje_descuento=100
valor_pagar=valor_compra-((porcentaje_descuento*valor_compra)/100)
print("El cliente debe pagar: $", valor_pagar)
