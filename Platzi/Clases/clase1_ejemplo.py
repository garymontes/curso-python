


class Transporte():
    '''Descripción de la forma de transportame desde casa al trabajo'''
    
    def __init__(self,moto, cole, pc):
        self.mototaxi=moto
        self.colectivo=cole
        self.pasacaballos=pc



if __name__=='__main__':
    viaje1=Transporte(1000,5000,3400)
    print(f'Los datos del viaje 1 son: {viaje1.__dict__}')