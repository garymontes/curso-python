'''
Crea una clase base Animal con un método hacer_sonido. Luego, crea dos clases derivadas Perro y Gato que sobreescriban el método hacer_sonido.

Define la clase Animal con un método hacer_sonido.

Define la clase Perro que herede de Animal y sobreescriba el método hacer_sonido para ladrar.

Define la clase Gato que herede de Animal y sobreescriba el método hacer_sonido para maullar.

Crea instancias de Perro y Gato, y llama al método hacer_sonido.
'''


class Animal():
    def __init__(self, nombre):
        self.nombre=nombre

    def hacer_sonido(self):
        return 'Sonido del animal'
    
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hacer_sonido(self):
        return 'Guau Guau'


class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        return 'Miau Miau'

perro=Perro('Firulais')
print(perro.hacer_sonido())  

gato=Gato('Garfield')
print(gato.hacer_sonido())