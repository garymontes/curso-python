class Persona:
    
    '''programa crea una clase con los datos pesonales de una persona'''
    
    '''def __init__(self,nombre, edad, sexo, correo,pais, ciudad, empleo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.correo=correo
        self.pais=pais
        self.ciudad=ciudad
        self.empleo=empleo

    def descripcion(self):
        return (f'{self.nombre} tiene: {self.edad} años, sexo: {self.sexo}, correo: {self.correo}, pais: {self.pais}, vive en: {self.ciudad} y su profesión es: {self.empleo}')
'''
class Gente:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def g(self):
        print(f'El nombre es: {self.nombre} {self.apellido} y su edad es: {self.edad} años')


def run():
    persona1=Persona('Gary Montes',41,'masculino','gary.montes@hotmail.com','colombia','cartagena','ingeniero')
    print(persona1.descripcion())

    persona2=Persona('Susy Montes',10,'femenino','susy.montes@hotmail.com','colombia','cartagena','estudiante')
    print(persona2.descripcion())

def llamado():
    per1=Gente('Gary', 'Montes', 41)  
    per2=Gente('Susy', 'Montes', 9) 
    per1.g()
    per2.g()
      


if __name__=='__main__':
    llamado()
    print('-'*30)