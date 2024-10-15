# Números primos: Escribe un programa que encuentre todos los números primos entre 1 y 100

a=int(input('Escriba un número entre dire si es primo: '))


for i in range(2,a):
    if a % i==0:
        print(f'El número {a} no es primo')
        break
    else:
        print(f'El número {a} es primo')
        break


    