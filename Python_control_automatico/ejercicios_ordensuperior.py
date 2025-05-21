from functools import reduce
con=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
fon=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
p=['yuca','mamey', 'comfenalco','tecnologico', 'gary', 'semestre']



def tra():
    '''
    Transformación de lista Escribe una función que tome una lista de números 
    y devuelva una nueva lista con cada número elevado al cuadrado. Usa map.
    '''
    a=list(map(lambda x:x**2, con))
    print(a)
    print('-'*20)
    a_fil=list(filter(lambda x:x%2==0,a))
    print(a_fil)

def pal():
    '''
    Filtrado de palabras Dada una lista de palabras, usa filter para obtener solo aquellas que tienen más de cinco letras.
    '''   
    a=list(filter(lambda x:len(x)>4, p)) 
    print(a)
    
def comp():
    '''
    Reducción de precios Supón que tienes una lista de precios de productos. Usa reduce para calcular el precio total de todos los productos.
    '''
    u=reduce(lambda a,b: a+b, fon)
    print(f'La suma total de la lista de precio es: {u}')
    


if __name__=='__main__':
    comp()