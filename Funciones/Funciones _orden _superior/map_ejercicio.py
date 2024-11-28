# Ejercicio con map(function, iterable)
def m():
    l=[16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
    n=list(map(lambda x: x**2, l))
    print(f'La lista utilizando map es: {n}')


if __name__=='__main__':
    print('')
    m()
    
    
    print('')
    
