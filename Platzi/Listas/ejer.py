# tablas de multiplicar
'''a=int(input('Ingresesa la tabla que deseas multiplicar: '))


for i in range(1,11):
    print(f'{i} x {a} = {i*a}')'''

print('-'*30)

# Sumar elementos de una lista: Dada una lista de números, escribe un programa que calcule la suma de todos los elementos de la lista.
c=int(input('Ingrese el tamaño de la lista: '))
lista=[]
suma=0

for i in range(c):
   a=int(input(f'Ingrese el valor número {i} a la lista: '))
   lista.append(a)
   suma=suma+lista[i]
   
print(f'Los valores de la lista son los siguientes: {lista}')


print(f'La suma total de la lista es: {suma}')