#Diccionarios comprehension
print()
def dc():
    diccionario={
        'milk':0.75,
        'meat':1039,
        'eggs':2.14,
        'bread':1.07
    }
    
    print(f'El diccionario original es {diccionario}')
    print('-'*50)
   
    for i,j in diccionario.items():
        print(f'{i} - {j**2}')
        diccionario[i]=j**2
        
    print(f'El nuevo diccionario es: {diccionario}')
     
    dic2={a:b**2 for a,b in diccionario.items()}
    print(f'Utilizando diccionarios comprehension: ')
    print(f'{dic2}')
   
    print('\n')


if __name__=='__main__':
    dc()