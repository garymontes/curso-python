

def conteo(n):
    print(f'n es: {n}')
    if n >0:
        conteo(n-1)
    

a=input('Ingrese un número: ')
if a.isnumeric():
    n=int(a)
    conteo(n)
else:
    print('Error, vuelve a intentarlo')