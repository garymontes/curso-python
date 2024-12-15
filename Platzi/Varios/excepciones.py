def run():
    while True:
        try:
            x= float(input('Digite el primer número: '))
            y= float(input('Digite el segundo número: '))
            if y < 0:
                raise ZeroDivisionError
            return x/y
            
        except ValueError: print("Por favor, ingresa números válidos.")
        except ZeroDivisionError as e:print('No se puede dividir por cero o números negativos')
        

       
    
  


if __name__=='__main__':
    print('')
    a=run()
    if a is not None:
        print(f'El resultado de la operación es: {a}')
    print('-'*30)
   


