class Forma():
    def __init__(self,area,perimetro):
        self.area=area
        self.perimetro=perimetro

class Triangulo(Forma):
    def calculaArea(self,base,altura):

        self.area=base+altura**2
        print(f"o valor da area  dp triangulo é: {self.area}")

class Retangulo(Forma):
    def calcularPerimetro(self,base,altura):
        self.perimetro=(base+altura)**2
        print(f"o valor da area do perimetro é: {self.perimetro}")

