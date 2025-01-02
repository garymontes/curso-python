


class Empleado():
    def __init__(self, nombres, apellidos, edad, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.salario = salario
    def __str__(self):
        return f"El empleado {self.nombres} {self.apellidos} tiene {self.edad} años y su salario es de {self.salario}"

class Empleador():
    def __init__(self, empresa, nit):
        self.empresa = empresa
        self.nit = nit
    def __str__(self):
        return f"trabaja para la empresa {self.empresa} con NIT {self.nit}"

class Cesantias(Empleado, Empleador):
    def __init__(self, nombres, apellidos, edad, salario, empresa, nit, nombre_fondo):
        super().__init__(nombres, apellidos, edad, salario)
        Empleador.__init__(self,empresa,nit)
        self.nombre_fondo = nombre_fondo
    def __str__(self):
        return f' {super().__str__()}, {Empleador.__str__(self)} tiene las cesantias en: {self.nombre_fondo}'
    
class ARL(Empleado, Empleador):
    def __init__(self, nombres, apellidos, edad, salario, empresa, nit, nombre_arl):
        super().__init__(nombres, apellidos, edad, salario)
        Empleador.__init__(self,empresa,nit)
        self.arl=nombre_arl

    def __str__(self):
        return f'{super().__str__()} {Empleador.__str__(self)} y está afiliado a la ARL: {self.arl}'

class Caja():
    def __init__(self,nombre_caja, categoria):
        self.nombre_caja=nombre_caja
        self.categoria=categoria

    def __str__(self):
        return f'La caja de compensación: {self.nombre_caja} tiene una categoria: {self.categoria}'

class Eps():
    def __init__(self, nombre_eps, ips):
        self.nombre_eps=nombre_eps
        self.ips=ips
    def __str__(self):
        return f'La EPS es: {self.nombre_eps} y su IPS es: {self.ips}'

class Ss(Caja, Eps):
    def __init__(self, nombre_caja, categoria, nombre_eps, ips,status):
        super().__init__(nombre_caja, categoria)
        Eps.__init__(self,nombre_eps, ips) 
        self.status=status  
    def __str__(self):
        return f'{super().__str__()} {Eps.__str__(self)} y se encuentra: {self.status} '
        


if __name__ == '__main__':

    empleado1= Cesantias('Gary', 'Montes', 41, 2845608, 'Telemática', 2222, 'Colpesiones')
    print(empleado1)

    empleado2=ARL('Susana', 'Montes', 9, 2000, 'Santa Clara', 1, 'Seguros Bolivar')
    print(empleado2)

    empleado3=Ss('Comfenalco', 'B', 'Sura', 'El Castillo', 'Activo')
    print(empleado3)