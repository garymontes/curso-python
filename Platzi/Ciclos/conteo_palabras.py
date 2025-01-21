# Contar palabras en una frase


def conteo():
    f=input('Ingrese una frase: ')
    a=f.split()
    b=0

    for i in a:
        b+=1
    print(f'El número de palabras en {a} es {b}')
    

if __name__=='__main__':
    conteo()