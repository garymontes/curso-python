from math import factorial, sqrt, ceil
a=8
print('')

print(f'El factorial de {a} es igual a: {factorial(a)}')
print('')

b=int(input('Ingrese un numero para calcular la raiz cuadrada: '))
print(f'La raiz cuadrada de {b} es: {sqrt(b)}')
b=ceil(sqrt(b))
print(f'Redondeando: {b}')
print('')