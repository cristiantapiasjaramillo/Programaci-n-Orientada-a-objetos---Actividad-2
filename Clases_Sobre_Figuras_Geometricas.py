import math

class Circulo:


  def __init__(self, radio):

    self.radio   = radio


  def calcularArea(self):
      return (math.pi * (self.radio**2) )


  def calcularPerimetro(self):
    return (2*math.pi*self.radio)

class Rectangulo:


  def __init__(self, base, altura):

    self.base   = base
    self.altura = altura


  def calcularArea(self):
      return (self.base * self.altura )


  def calcularPerimetro(self):
    return ((2*self.base) + (2*self.altura))

class Cuadrado:


  def __init__(self, lado):

    self.lado  = lado


  def calcularArea(self):
      return (self.lado * self.lado )
  

  def calcularPerimetro(self):
    return (4 * self.lado)

class TrianguloRectangulo:

  def __init__(self, base, altura):

    self.base   = base
    self.altura = altura


  def calcularArea(self):
      return ((self.base * self.altura)/2 )
 

  def calcularPerimetro(self):
    return (self.base + self.altura + self.calcularHipotenusa())


  def calcularHipotenusa(self):
    return math.sqrt(((self.base**2) + (self.altura**2)))


  def determinarTipoTriangulo(self):
    if((self.base == self.altura) and (self.base == self.calcularHipotenusa())
     and (self.altura == self.calcularHipotenusa())):
      
      print("Es un triangulo equilatero")
    
    elif ((self.base != self.altura ) and (self.base != self.calcularHipotenusa())
          and (self.altura != self.calcularHipotenusa())):
      
      print("Es un triangulo escaleno")

    else:

      print("Es un triangulo isoceles")

class Rombo:

  def __init__(self, diagonal_menor, diagonal_mayor):
    self.diagonal_menor = diagonal_menor
    self.diagonal_mayor = diagonal_mayor


  def calcularLado(self):
   
    cateto1 = self.diagonal_menor/2
    cateto2 = self.diagonal_mayor/2
    return math.sqrt(((cateto1**2) + (cateto2**2)))


  def calcularArea(self):
    return (self.diagonal_menor * self.diagonal_mayor)/2

  def calcularPerimetro(self):
    return 4*self.calcularLado() 

class Trapecio:


  def __init__(self, base1, base2, altura):
    self.base1 = base1
    self.base2 = base2
    self.altura = altura


  def calcularArea(self):
    return ((self.base1+self.base2)/2)*self.altura


  def calcularPerimetro(self):

    return 2*self.calcularDiagonal() + self.base1 + self.base2


  def calcularDiagonal(self):
    cateto = abs(self.base1-self.base2)
    return math.sqrt(((cateto**2) + (self.altura**2)))
  

class PruebaFiguras:

  def main(self):
    figura1 = Circulo(2)
    figura2 = Rectangulo(1,2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3,5)
    figura5 = Rombo(12,16)
    figura6 = Trapecio(12,15,6)

    print(f"El area del circulo es = {figura1.calcularArea()}")
    print(f"El perimetro del circulo es = {figura1.calcularPerimetro()}\n")
    print(f"El area del rectangulo es = {figura2.calcularArea()}")
    print(f"El Perimetro del rectangulo es = {figura2.calcularPerimetro()}\n")
    print(f"El area del cuadrado es = {figura3.calcularArea()}")
    print(f"El perimetro del cuadrado es = {figura3.calcularPerimetro()}\n")
    print(f"El area del triangulo es = {figura4.calcularArea()}")
    print(f"El perimetro del triangulo es = {figura4.calcularPerimetro()}\n")
    figura4.determinarTipoTriangulo()
    print(f"El perimetro del rombo es = {figura5.calcularPerimetro()}")
    print(f"El area del rombo es = {figura5.calcularArea()}\n")
    print(f"El perimetro del trapecio es = {figura6.calcularPerimetro()}")
    print(f"El area del Trapecio es = {figura6.calcularArea()}")

Prueba = PruebaFiguras()

Prueba.main()
