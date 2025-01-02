# Ejercicio de herencia múltiple


class Familia():
    def __init__(self, nombre, primer_apellido, segundo_apellido, edad, padre, madre):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.edad = edad
        self.padre = padre
        self.madre = madre
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.primer_apellido} {self.segundo_apellido}, Edad: {self.edad}, Padre: {self.padre}, Madre: {self.madre}"

class Hijos(Familia):
    def __init__(self, nombre, primer_apellido, segundo_apellido, edad, num_hermanos, padre, madre, hermanos):
        super().__init__(nombre, primer_apellido, segundo_apellido, edad, padre, madre)
        self.num_hermanos = num_hermanos   
        self.hermanos = hermanos


if __name__== '__main__':
    a = input('Ingrese el nombre del hijo: ')
    b = input('Ingrese el primer apellido del hijo: ')
    c = input('Ingrese el segundo apellido del hijo: ')
    d = int(input('Ingrese la edad del hijo: '))
    e = int(input('Ingrese el número de hermanos del hijo: '))
    f = input('Ingrese el nombre del padre: ')
    g = input('Ingrese el nombre de la madre: ')
    h = [input(f'Ingrese el nombre del hermano {i+1}: ') for i in range(e)]
    
    hijo = Hijos(a, b, c, d, e, f, g, h)
    print(f'{hijo} y sus hermanos son: {h}')
    