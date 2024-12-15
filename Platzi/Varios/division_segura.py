#Escribe una función que tome dos números como entrada y devuelva su cociente. Maneja la excepción cuando el divisor es cero

def division():
    while True:
        try:

            b=float(input('Ingrese el primer número: '))
            c=float(input('Ingrese el segundo número: '))
            if c==0:
                raise ZeroDivisionError('No se puede dividir sobre 0')
            return b/c
        except ValueError: print('Error, por favor ingresa valores validos')
        except ZeroDivisionError as e: print(f'Error! {e} Intentalo de nuevo.')



if __name__=='__main__':
    print('')
    a=division()
    
    print(f'El cociente es: {a}')