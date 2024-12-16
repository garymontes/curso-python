# Escribe una función que convierta una lista de cadenas en una lista de enteros. Maneja la excepción cuando la conversión falla
def run():
    while True:
        try:
            lista_cadenas=input('Ingrese la lista de números: ')
            enteros= [int(i) for i in lista_cadenas]
            print(f'La lista de número es: {enteros}')
            break
        except ValueError: print('Error, por favor ingresa números validos')
            



if __name__=='__main__':
    run()