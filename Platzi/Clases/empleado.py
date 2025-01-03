


class Empleado():
    def __init__(self, nombre, salario):
        self.nombre=nombre
        self.salario=salario
    
    def __str__(self):
        return f'Nombre: {self.nombre}, tiene un salario de: {self.salario}'


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre,salario)
        self.departamento=departamento
    
    def __str__(self):
        return f'{super().__str__()} y pertenece al Ddepartamento: {self.departamento}'

gerente=Gerente('Gary Montes', 2800000, 'Soporte Sistemas')
print(gerente.__str__())

