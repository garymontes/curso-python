# Suma de números: Escribe un programa que sume los números del 1 al 10 
'''n=0
for i in range(11):
    n+=i
    print(n)'''
    
# Lista de cuadrados: Genera los cuadrados de los primeros 10 números naturales y almacénalos en una lista

'''l=[]
for i in range(11):
    print(f'El cuadrado de {i} es: {i**2}')
    l.append(i**2)
    
print(f'Los número al cuadrado de la lista son: {l}')'''

# Tablas de multiplicar: Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10.

'''numero=(input('Ingrese un número y haré la tabla de multiplicar: '))
if numero.isdigit():
    m=int(numero)
    for i in range(11):
        print(f'{m} x {i} = {i*m}')
else:
    print('Error, debe ingrese un número. Vuelva a intentarlo')
    ''' 
lista = list(range(11))
print(lista)
lista2= [i for i in lista]
print(lista2)