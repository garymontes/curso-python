print('')
objetos=[7,'hola', True, 3.5]
print(f'La lista es {objetos}')

for i in range(len(objetos)):
    print(f'Un elemento de la lista es: {objetos[i]}')
print('-'*30)
a=objetos[::-1]
print(f'La nueva lista es {a}')

for i in range(len(a)):
    print(a[i])

objetos.append(90)
print(objetos)
objetos.extend(a)
print(f'La nueva lista añadida es: {objetos}')

print('')