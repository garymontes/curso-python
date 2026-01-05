# programa que convierte los elementos de una lista en mayusculas, utilizando funciones de orden superior map
my_pets = ['alfred', 'tabitha', 'william', 'arla']
m=list(map(lambda x: x.upper(), my_pets))
print(m)

