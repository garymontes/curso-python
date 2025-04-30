# Multiplicar por 3: Crea una función lambda que reciba un número y devuelva ese número multiplicado por 3.

def multiplica_3():
    a=(input('Escriba un número: '))
    if a.isdigit():
        a=int(a)
        b=lambda a,c:a*c
        print(f'El número multiplicado por 3 es: {b(a,3)}')
    else:
        print('Error, debe escribir un número.')
    
def suma_2():
    a=int(input('Escriba el primer número: '))
    b=int(input('Escriba el segundo número: '))
    sum= lambda a,b: a+b
    print(sum(a,b))

def convertir_mayus():
    l=input('Escriba un texto: ')
    c= lambda l: l.upper()
    print(c(l))

# Par o impar Usa una función lambda para verificar si un número es par o impar. Debería devolver True para números pares y False para impares
def par_impar():
    a =int(input('Escriba un número: '))
    
    o = lambda a: a%2==0
        
    if o(a):
        print('True')
    else:
        print('False')


if __name__=='__main__':
    par_impar()
    
    