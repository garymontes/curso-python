# Crea un programa que permita almacenar, buscar y eliminar contactos en una agenda telefónica utilizando un diccionario
print('\n')
agenda={}

def agregar_contacto():
    n=(input('Ingrese nombre del contacto: '))
    a=(input('Ingrese apellido del contacto: '))
    t=int(input('Ingrese el número de teléfono: '))
    print(f'El contacto agregado es: {n} {a} tel.: {t}')
    for i in range(3):
        agenda['Nombre']=n
        agenda['Apellido']=a
        agenda['Número telefónico']=t
    print(f'el contacto agregado es: {agenda.items()}')
    
    print('-'*50)
    
    for i,j in agenda.items():
        print(f'{i}: {j}')

    

def buscar_contacto():
    pass

def eliminar_contacto():
    pass




if __name__=='__main__':
    agregar_contacto()

print('\n')