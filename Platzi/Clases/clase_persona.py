class Persona:
    
    '''programa crea una clase con los datos pesonales de una persona'''
    
    def __init__(self,nombre, edad, sexo, correo,pais, ciudad, empleo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.correo=correo
        self.pais=pais
        self.ciudad=ciudad
        self.empleo=empleo

    def descripcion(self):
        return (f'{self.nombre} tiene: {self.edad} años, sexo: {self.sexo}, correo: {self.correo}, pais: {self.pais}, vive en: {self.ciudad} y su profesión es: {self.empleo}')


def run():
    persona1=Persona('Gary Montes',41,'masculino','gary.montes@hotmail.com','colombia','cartagena','ingeniero')
    print(persona1.descripcion())

    persona2=Persona('Susy Montes',10,'femenino','susy.montes@hotmail.com','colombia','cartagena','estudiante')
    print(persona2.descripcion())

    


if __name__=='__main__':
    run()