for i in range(11):
    print(i*i)
print('-'*20)

a='curso de python'
for i in a:
    print(i)

# Escribe un programa que imprima todos los números impares del 1 al 20

b=int(input('Ingresa un numero par: '))

for i in range(b+1):
    if i%2==0:
        print(f'{i} es un número par de {b}')
print('Fin de los número pares')