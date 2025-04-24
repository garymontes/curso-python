


def cuadrados():
    '''Cuadrados de números:
    Crea un diccionario donde las claves sean los números del 1 al 5 y los valores sean sus cuadrados.
    '''
    di={i:i**2 for i in range(1,6)}
    print(di)
    
def filtrado():
   ''' palabras='gary', 'montes', 'bracamonte', 'cartagena', 'colombia', 'susanita', 'olier', 'consuelo', 'jesus'
    #print(f'Las palabras son: {palabras}')
    
    dici={i:len(i) for i in palabras if len(i)>=4}
    print(dici.items())'''
    
def multiplicacion():
    '''Multiplicación de valores:
        Dado un diccionario con valores numéricos, genera uno nuevo con los mismos claves pero multiplicando sus valores por 2. 
    '''
    numeros={
        '00':13,
        '01':67,
        '03':100
    }
    num_mult={i:j*2 for i,j in numeros.items()}
    print(num_mult.items())


if __name__=='__main__':
    multiplicacion()