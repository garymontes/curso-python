# Ejercicio de una tabla que contiene utiles escolares

def run():
    
    tienda={
        'item':['lapiz','carpeta','marcador'],
        'cantidad':[5,4,3],
        'valor':[4.15,8.5,9.2]
    }
    
    print('')
    tienda['genero']='m'
    tienda['etnia']='ninguna'
    print(f'Los datos de la tienda son: {tienda}')
    print('\n')
    
    
    for i in tienda:
        print(f'{i}: {tienda[i]}')
    print('')
    print(tienda.values())
    print(tienda.keys())
    print(tienda.items())
    print('-'*50)
    
    for i,j in tienda.items():
        print(f'{i} - {j}')



if __name__=='__main__':
    run()
    
    print('\n')