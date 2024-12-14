# Ejercicios varios utilizando lambda 
print()
def suma():
    
    suma= lambda a,x : a+x
    print(suma(4,5))

def resta():
    
    resta= lambda b,c : b-c
    print(f'La resta de la función Lamba es: {resta(10,8)}')
    
def multiplicacion():
    mult= lambda a,x : a*x
    print(f'La multiplicación es: {mult(5,5)}')
    
def division(a,b):
    return lambda: a/b
    #divi= lambda a,b: a/b
    #print(f'La división es: {divi(100,50)}')
    
    

    print()
if __name__=='__main__':
    x=int(input('Ingrese el numerador: '))
    y=int(input('Ingrese el denominador: '))
    div=division(x,y)
    print(f'El resultado es: {div()}')
    #division()
    

