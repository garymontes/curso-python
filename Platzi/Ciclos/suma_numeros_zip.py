'''
Suma de Elementos Correspondientes
Tienes dos listas de números. Usa zip para sumar los elementos correspondientes de ambas listas y 
obtener una nueva lista con los resultados.
'''

def suma():
    a=[56,8,4,3,1]
    b=[100,7,0,3,41]
    #print(f'La lista 1 es: {a} y la lista 2 es: {b}')

    c=[a+b for a,b in zip(a,b)]
    print(c)
    




if __name__=='__main__':
    suma()