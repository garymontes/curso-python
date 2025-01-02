'''programa que cree dos super clases, una será empleado que pida por consola el nombre del empleado en un método de instancia. La segunda clase será salario
y pedirá por consola el salario del empleado en un metedo de instancia. 
crea una clase hija llamada Designación que herede las dos clases anteriores y que tenga un método que designe el cargo del empleado.
verifica el código, instanciando un objeto de la clase hija, verificando si el objeto tiene el método nombre y salario.
'''


class Empleado:
    def __init__(self):
        self.nombre = input('Ingrese el nombre del empleado: ')

class Salario:
    def __init__(self):
        self.salario = input('Ingrese el salario del empleado: ')

class Designacion(Empleado, Salario):
    def __init__(self, cargo):
        Empleado.__init__(self)
        Salario.__init__(self)
        self.cargo = cargo
        
    def __str__(self):
        return f'El empleado {self.nombre} tiene un salario de {self.salario} y su cargo es {self.cargo}'

if __name__ =='__main__':
    a=input('Ingrese el cargo del empleado: ')
    empleado=Designacion(a)
    print(empleado)      
        