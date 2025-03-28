# Operaciones aritmeticas utilizando un menú

def operaciones():
    a=int(input('Digite el primer número: '))
    b=int(input('Digite el segundo número: '))
    print(f'los números son: {a} y {b}')

    suma=(a+b)
    print(f'La suma es: {suma}')
    resta=(a-b)
    print(f'La resta es: {resta}')
    multiplicacion=(a*b)
    print(f'La multiplicación es: {multiplicacion}')
    division=(a/b)
    print(f'La division es: {division}')
    modulo=(a%b)
    print(f'El módulo es: {modulo}')

    t=0,1,2,3,4
    print(t)
    print(type(t))




if __name__=='__main__':
    print()
    operaciones()
    print()