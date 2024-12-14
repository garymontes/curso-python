# Crear dos funciones anonimas:
# reciba un valor en farenheit y retorne el valor en celcius
# reciba un valor en celcius y retorne el valor en farenheit
'''
    
'''
print('')

def far_cel():
    y=float(input('Ingrese el valor de y: '))
    f=float(input('Ingrese el valor a x: '))
    return lambda: (y-f)*5.0/9.0

    
    
    




if __name__=='__main__':
   
    conv=far_cel()
    print(f'El resultado de la conversión es: {conv()}')
    
    print('')
    