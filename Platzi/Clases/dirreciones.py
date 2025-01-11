


class Direccion():
    def __init__(self, calle, ciudad, pais):
        self.calle=calle
        self.ciudad=ciudad
        self.pais=pais

    def __str__(self):
        return f'Calle:{self.calle}, Ciudad:{self.ciudad}, Pais:{self.pais}'


class Persona(Direccion):
    def __init__(self, nombre, edad,calle, ciudad, pais):
        super().__init__(calle, ciudad, pais)
        self.nombre=nombre
        self.edad=edad
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Vive en{super().__str__()}'

class Empleado(Persona):
    def __init__(self, nombre, edad, calle, ciudad, pais):
        super().__init__(nombre, edad,calle, ciudad, pais)
    
    def __str__(self):
        return f'{super().__str__()}'
    
dir1=Empleado('Gary Montes',41, 'Frente a la Panadería', 'Cartagena', 'Colombia')
print(dir1.__str__())