'''
Crea una clase Estudiante que tenga los siguientes atributos y métodos:
Atributos: nombre, edad, grado
Métodos:
mostrar_informacion(): muestra el nombre, la edad y el grado del estudiante
es_mayor_de_edad(): devuelve True si el estudiante tiene 18 años o más, de lo contrario, False
'''
class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    
    def mostrar_informacion(self):
        return(f'Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}')
    
    def es_mayor_de_edad(self):
        if self.edad>=18:
            return True
        else:
            return False

alumno=Estudiante('Gary Montes',41,'9')
print(alumno.mostrar_informacion())
print(alumno.es_mayor_de_edad())