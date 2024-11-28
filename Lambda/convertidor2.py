# programa que convierte grados Farenheit a Celsius y viceversa

def con():
    c=float(input('Ingrese los grados Farenheit a convertir en Celcius: '))
    return lambda : (5/9)*(c-32)
   
def cel():
    f=float(input('Ingrese los grados Celcius a convertir en Farenheit: ')) 
    return lambda: 9/5*(f+32) 
    


if __name__=='__main__':
    a=con()
    print(f'La conversión de grados farenheit a celcius es: {a():.2f}')
    
    b=cel()
    print(f'La conversión de grados Celcius a farenheit es: {b():.2f}')
    
    print('')
