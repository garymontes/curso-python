# # Crear una lista de los cuadrados de los números del 1 al 10
print('')

def lcuadrados():
    
    num=[1,2,3,4,5,6,7,8,9,10]
    print(f'La lista original es: {num}')
    global a
    global b
    b=[i*2 for i in num]
    a=[print(f'El cuadrado de {i} es: {(i**2)}') for i in num]
    
def num_pares():
    # # Crear una lista de números pares del 1 al 20
    print('')
    global c
    c=list(range(1,21))
    d=[i for i in c if i%2==0]
    print(d)
    print('\n')
    
def mayus():
    # Convertir todas las palabras de una lista a mayúsculas
    palabra=input('Introduzca una palabra: ')
    palabra = list(palabra)
    print(f'La palabra es: {palabra}')
    a=[i.upper() for i in palabra]
    print(a)
    
def primera_letra():
    # Extraer la primera letra de cada palabra en una lista
    lista=['susana','susy', 'gary', 'montes']
    print(f'La lista original es: {lista}')
    print('')
    a=[i[0].upper() for i in lista]
    print(f'La primera letra de cada palabra de la lista es: {a}')
    print('-'*60)
    b=[i[1] for i in lista]
    print(f'La nueva lista en b es: {b}')
  
         
    
    
    print('')
    
    


if __name__=='__main__':
    num_pares()
    
