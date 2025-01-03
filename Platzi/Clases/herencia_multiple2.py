


class Estudiante():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def estudiar(self):
        return f'El estudiante: {self.nombre}, tiene {self.edad} años'

class Deportista():
    def __init__(self, deporte):
        self.deporte=deporte
    
    def entrenar(self):
        return f'y su deporte favorito es: {self.deporte}'

class EstudianteDeportista(Estudiante, Deportista):
    def __init__(self,nombre, edad, deporte):
        super().__init__(nombre, edad)
        Deportista.__init__(self,deporte)
    
    def estudiar_entrenar(self):
        return f'{super().estudiar()} {Deportista.entrenar(self)}' 
        
e=EstudianteDeportista('Gary Montes', 41 ,'Beisbol')
print(e.estudiar())
print(e.estudiar_entrenar())
