# programa que calcula el factorial de un número
n=int(input('Digite un numero para calcular su factorial: '))
f=1
c=1 # controla el ciclo while con cada iteración
print('')

while c <=n: 
    f=f*c 
    print(f'Factorial ahora vale: {f}')
    c=c+1 
    print(f'El ciclo c vale: {c}')
    print('---'*20)
print('')
print(f'El factorial de {n} es: {f}')