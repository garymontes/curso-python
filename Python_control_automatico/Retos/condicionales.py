'''
- Número positivo o negativo
- Pide un número al usuario y determina si es positivo, negativo o cero.
'''
print(' ')
a=int(input('Ingrese un número: '))

if a == 0:
    print(f'El número ingresado es: {a} ')
elif a>=0:
    print(f'el número {a} es positivo')
elif a<0:
    print(f'El número {a} es negativo')

print(' ')
print('Fin del programa')
print(' ')