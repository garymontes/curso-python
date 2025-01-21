'''
Encontrar el número máximo en una lista:
Crea una lista de números.
Utiliza un ciclo for para encontrar el número máximo en la lista
'''

def num_maximo():
    numeros=[1052,547,1,9875,6587,102,41,9,38,150,11254,745896]
    print(f'La lista de números es: {numeros}')
    maximo=numeros[0]

    for i in numeros:
        if i > maximo:
            maximo=i
            
    print(f'El número máximo es: {maximo}')
    



if __name__=='__main__':
    num_maximo()