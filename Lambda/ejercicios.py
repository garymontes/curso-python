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

    print()
if __name__=='__main__':
    multiplicacion()

