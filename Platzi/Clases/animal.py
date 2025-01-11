


class Animales():
    def __init__(self, animal):
        self.animal=animal
    
    def comiendo(self):
        print (f'El {self.animal} está comiendo')
    
    def durmiendo(self):
        print (f'El {self.animal} está durmiendo')
    
class Carnivoro(Animales):
    def __init__(self, animal_carnivoro):
        super().__init__(animal_carnivoro)

    def comiendo(self):
        print (f'El {self.animal} está comiendo carne')
   

if __name__=='__main__':
    perro=Animales('Pitbull')
    perro.comiendo()
    perro.durmiendo()

    porcino=Carnivoro('Cerdo')
    porcino.comiendo()