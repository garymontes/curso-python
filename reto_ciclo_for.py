# Entre todos los números en el intervalo de 1 hasta 100, se pide contar los numeros que son mulitplos de 4
# y mostrar la suma de todos los números multiplos de 4.
print('')
a=b=0
for i in range(1,101):
    if i%4==0:
        print(f'4 es multiplo de: {i}')
        b=b+1
        a=i+a 
    continue
print('')
print(f'en total hay {b} numeros que son multiplos de 4 y cuya suma es igual a: {a}')
print('')