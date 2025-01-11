from math import pi


class Figura():

    def __init__(self, figura):
        self.figura=figura

    def calcular_area(self):
        print(f'El area del {self.figura} es:')

    def __str__(self):
        return (f'{self.figura}')

class Circulo(Figura):

    def __init__(self, radio_balon):
        super().__init__('Circulo')
        self.radio_balon=radio_balon

    def calcular_area(self):
        print(f'El area del Circulo es: {(pi*self.radio_balon**2):.2f}')        
     
    
class Rectangulo(Figura):
    def __init__(self, ancho, largo):
        super().__init__('Rectangulo')
        self.ancho=ancho
        self.largo=largo

    def calcular_area(self):
        print(f'El area del {self} es: {self.ancho*self.largo}')

if __name__=='__main__':
    figura1=Figura('Triangulo')
    figura1.calcular_area()

    figura2=Circulo(15)
    figura2.calcular_area()

    figura3=Rectangulo(5,8)
    figura3.calcular_area()