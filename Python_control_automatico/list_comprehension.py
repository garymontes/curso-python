'''# Cuadrados de números: Crea una lista con los cuadrados de los números del 0 al 9.
a=[i**2 for i in range(10)]
print(a)'''

'''# Filtrar números pares: Genera una lista con los números pares del 0 al 20
b=[i for i in range(21) if i % 2 == 0]
print(f'Los números pares son: {b}')'''

# Transformar palabras: Convierte todas las palabras de una lista a mayúsculas.
'''palabras=['bienvenidos', 'a', 'cartagena']
print(palabras)'''

'''mayus=[i.upper() for i in palabras ]
print(mayus)
'''
# Filtrar palabras por longitud: Crea una lista con palabras de más de 5 letras
palabras=['Cartagena','Susana', 'Margarita', 'Susy', 'Gary', 'Candy']

f= [i for i in palabras if len(i)>5]
print(f)