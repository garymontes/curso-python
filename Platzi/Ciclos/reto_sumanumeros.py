'''
Sumar una lista de números:
Crea una lista de números.
Utiliza un ciclo for para sumar todos los números de la lista
'''
def suma():
    l=[89,45,2,4,9,34,91,1,0,115]
    print(f'La lista inicial es: {l}')
    a=0

    for i in l:
        a+=i
    print(f'La suma de todos los números es: {a}')

if __name__=='__main__':
    suma()

