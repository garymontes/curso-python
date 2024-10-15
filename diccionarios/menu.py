# Programa que muestra un menú para la edición, consulta, registro e impresión de una agenda utilizando diccionarios
print('')

agenda={
    'gary':{
        'cc':73,
        'tel':305,
        'email':'gary@gmail.com',
        'dir':'santa clara',
        'job':'ing sistemas',
        'hobbies':{
            'musica':['salsa', 'champeta', 'vallenato']
        }
    },
    'susana':{
        'cc':10,
        'tel':316,
        'email':'candy@gmail.com',
        'dir':'santa clara',
        'job':'licenciada',
        'hobbies':{
            'musica':['porro', 'champeta', 'vallenato']
        }
    },
    'susy':{
        'cc':108,
        'tel':300,
        'email':'susy@gmail.com',
        'dir':'santa clara',
        'job':'estudiante',
        'hobbies':{
            'musica':['salsa', 'cristiana', 'merengue']
        }
    }
}

def imprimir():
    print('1. Imprimir la agenda\nLos datos de la agenda son los siguientes:\n')
    for i,j in agenda.items():
        print(f'-- {i.capitalize()}:  {j}')
    
    for i,j in agenda.items():
        print(f'Los datos de hobbies de {i} son los siguientes:')
        for a,b in j['hobbies'].items():
            print(f'Los hobbies son: {a} - {b}')
    

def agregar():
    
    nom=input('Ingrese el nombre de la persona: ')
    agenda[nom]={}
    agenda[nom]['cc']=int(input(f'Ingrese el número de cedula de {nom.capitalize()}: '))
    agenda[nom]['tel']=int(input(f'Ingrese el número de teléfono de {nom.capitalize()}: '))
    agenda[nom]['email']=input(f'Ingrese el correo de {nom.capitalize()}: ')
    agenda[nom]['dir']=input(f'Ingrese la dirreción de {nom.capitalize()}: ')
    agenda[nom]['job']=input(f'Ingrese el trabajo de {nom.capitalize()}: ')
    musica=[]
             
    for i in range(3):
        musica.append(input('ingrese un genero musical: '))
    print(f'los hobbies de {nom.capitalize()} son: {musica}')
    
    agenda[nom]['hobbies']={'musica':musica}
    
    print()
    for i,j in agenda.items():
        print(f'-- {i.capitalize()}: {j}')    
       
    print()
    

def consultar():
    nom=input('Ingrese el nombre a consultar: ').strip().lower()
    if nom not in agenda:
        print(f'{nom.capitalize()} no esta en la agenda')
    else:
        print(f'el nombre {nom} si está en la agenda')
        print(f'Los datos de {nom} son los siguientes: {agenda[nom]}')
print()
    

def borrar():
    print('Borrar elementos de la agenda')
    
    
def salir():
    print('Salir')
    

def menus():
    print('''Programa que permite imprimir, agregar, consultar y borrar elementos de una agenda utilizando diccionarios:
           
        Presione:
        1. Imprimir la agenda
        2. Agregar elementos a la agenda
        3. Consultar elementos de la agenda
        4. Borrar elementos de la agenda
        5. Salir del programa
           ''')
    a=int(input('Escoja una opción: '))
    print('')
    
    if a == 1:
        imprimir()
        
    elif a == 2:
        agregar()
    
    elif a == 3:
        consultar()
    
    elif a == 4:
        borrar()
    
    elif a== 5:
        salir()
    
    else: 
        print('Número no valido, vuelva a intentarlo')
            
    
    print('\nFin\n')
    

if __name__=='__main__':
    menus()