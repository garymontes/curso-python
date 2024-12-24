# programa que controla las carreras en la universidad, gestión y control

class Universidad:
    '''Clase de universidad, se crean los atributos'''

    # Método constructor
    def __init__(self, carrera, estudiantes, semestre, docente, instalaciones):
        self.carrera=carrera
        self.estudiantes=estudiantes
        self.semestre=semestre
        self.docente=docente
        self.instalaciones=instalaciones
        
        
    
    def gestion_carreras(self,año=2025): # Crear, listar, adicionar, eliminar y gestionar las carreras
        if self.estudiantes>=20:
            print(f'El número de estudiantes matriculados {self.estudiantes}, si cumple para abrir un programa academico en el año {año}')
        else:
            print('No se puede abrir el curso por pocos estudiantes matriculados')
        
        


    def gestion_estudiantes(self): # Crear, listar, adicionar, eliminar y gestionar los estudiantes
        pass

    def gestion_empleados(self): # Crear, listar, adicionar, eliminar y gestionar los empleados
        pass
    
    def instalaciones_y_servicios(self): # Crear, listar, adicionar, eliminar y gestionar instalaciones y servicios
        pass

    
def run():
    programa=input('Ingrese el nombre de la carrera que desear consultar: ')
    num_estudiantes=int(input('Ingrese el número de estudiantes: '))
    sem=input('Ingrese el número de semestre: ')
    doce=input('Ingrese el nombre del docente: ')
    sede=input('Ingrese la sede: ')

    facultad1=Universidad(programa,num_estudiantes,sem, doce, sede)
    facultad1.gestion_carreras()
    print(f'La universidad Comfenalco en el programa {facultad1.carrera}, tiene matriculados {facultad1.estudiantes} estudiantes en {facultad1.semestre} semestre con el docente {facultad1.docente} en la sede {facultad1.instalaciones}')
    
 


if __name__=='__main__':
    run()