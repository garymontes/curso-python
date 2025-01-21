'''
Invertir una cadena:
Toma una cadena de texto.
Utiliza un ciclo for para invertir el orden de los caracteres en la cadena.
'''

def cadena():
    nombre='Gary Montes Bracamonte'
    print(f'La cadena es: {nombre}')
    nombre_invertido=''

    for i in nombre:
        nombre_invertido= i+nombre_invertido
        
    print(f'El nombre invertido es: {nombre_invertido}')

if __name__=='__main__':
    cadena()