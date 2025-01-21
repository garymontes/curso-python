# pruebas de ejercicios anidados utilizando ciclo for
print('\n')
def ani():
    a=[100,9,8]
    b=['a','b','c']
    print(f'La lista de números es: {a}')
    print(f'La lista de letras es: {b}')
    print('-'*50)
    for i in range(len(a)):
        print(f'En el ciclo {i} el número es: {a[i]}')
        print('Las letras son:')
        for j in range(len(b)):
                
                print(f'- {b[j]}')
    print('Fin del ciclo')


def per():
    a=[['Gary','Susana','Susanita'],['Bracamonte','Margarita','Olier'],[41,9,38]]
    for i in a:
        for j in i:
            print(f'{j}')
        print('-'*50)

def matriz():
    for i in range(1,5):
        for j in range(1,4):
            print(f'({i}-{j})', end=' ')
        print()

def mul():
    a=int(input('Ingrese el primer valor:'))
    b=int(input('Ingrese el segundo valor:'))
    
    for i in range(1,a+1):
        for j in range(1,b+1):
            print(f'{i} x {j} es: {i*j}')
        print('-'*50)


def per2():
    a=[['Gary','Susana','Susanita'],['Bracamonte','Margarita','Olier'],[41,9,38]]
    print(a)
    print('-'*50)


if __name__=='__main__':
    matriz()


print('\n')