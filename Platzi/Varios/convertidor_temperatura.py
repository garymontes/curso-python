# Escribe una función que convierta grados Fahrenheit a Celsius. Maneja la excepción cuando la entrada no es un número.
def run():
    while True:
        try:
            fac=float(input('Ingrese los grados farenheit para convertir a celcius: '))
            o= (fac-32)*5/9
            print(f'{fac} grados Farenheit corresponden a: {o:.2f}')
            break      
        except ValueError: print('Error, debes introducir un número valido.')
        
         
        


if __name__=='__main__':
    a=run()
    