'''
Sumar los números pares: Escribe un programa que sume todos los números pares entre 1 y n
donde n es proporcionado por el usuario.
'''

def numeros():
    n=int(input('Digite hasta que número desea encontrar los números pares: '))
    print(f'El número escogido es: {n}')
    np=0

    for i in range(n+1):
        if i%2==0:
            np+=i
            
    print(f'La suma de los números pares de {n} es: {np}')


if __name__=='__main__':
    numeros()