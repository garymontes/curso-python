def run():
    dicccionario={
        'str':'hola',
        'int':5,
        'float':3.14,
        'bool':True
        }
    print('')
    print(f'El diccionario es: {dicccionario}')
    print('')
    for i in dicccionario:
        print(f'La clave-valor es: {i}: {dicccionario[i]}')
    print('')
    
    dic={
        10:15,
        20:(9,8,7),
        'str':['gary','montes',41]
    }
    print(dic['str'][1].upper()[0])
    print(dic['str'][0].upper())
    print(dic['str'][2])
    print(f'Los elementos de la tupla son: {dic[20]}')
    
    print('\n')
    print('Las claves y valores del diccionario 2 son las siguientes: ')
    for i in dic:
        print(f'Clave-valor: {i,dic[i]}')
    
    print('\n')



if __name__=='__main__':
    run()
    