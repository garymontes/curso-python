# Función reduce(funcion, iterable)
from functools import reduce

def red():
    l=[1,2,3,4,5,6,7,8,9]
    r= reduce(lambda x,y : x+y,l)
    print(f'La suma acumulativa es: {r}')




if __name__=='__main__':
    print('')
    red()
    print('')