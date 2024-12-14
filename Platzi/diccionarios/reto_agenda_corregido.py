# Programa que muestra un menú para la edición, consulta, registro e impresión de una agenda utilizando diccionarios
agenda = {
    'gary': {
        'cc': 73,
        'tel': 305,
        'email': 'gary@gmail.com',
        'dir': 'santa clara',
        'job': 'ing sistemas',
        'hobbies': {
            'musica': ['salsa', 'champeta', 'vallenato']
        }
    },
    'susana': {
        'cc': 10,
        'tel': 316,
        'email': 'candy@gmail.com',
        'dir': 'santa clara',
        'job': 'licenciada',
        'hobbies': {
            'musica': ['porro', 'champeta', 'vallenato']
        }
    },
    'susy': {
        'cc': 108,
        'tel': 300,
        'email': 'susy@gmail.com',
        'dir': 'santa clara',
        'job': 'estudiante',
        'hobbies': {
            'musica': ['salsa', 'cristiana', 'merengue']
        }
    }
}

def imprimir():
    print('1. Imprimir la agenda\nLos datos de la agenda son los siguientes:\n')
    for nombre, datos in agenda.items():
        print(f'-- {nombre.capitalize()}:  {datos}')

def agregar():
    nom = input('Ingrese el nombre de la persona: ').strip().lower()
    if nom in agenda:
        print(f'{nom.capitalize()} ya está en la agenda.')
        return

    agenda[nom] = {}
    try:
        agenda[nom]['cc'] = int(input(f'Ingrese el número de cedula de {nom.capitalize()}: '))
        agenda[nom]['tel'] = int(input(f'Ingrese el número de teléfono de {nom.capitalize()}: '))
    except ValueError:
        print('Número inválido. Intente de nuevo.')
        return
    
    agenda[nom]['email'] = input(f'Ingrese el correo de {nom.capitalize()}: ').strip().lower()
    agenda[nom]['dir'] = input(f'Ingrese la dirección de {nom.capitalize()}: ').strip().lower()
    agenda[nom]['job'] = input(f'Ingrese el trabajo de {nom.capitalize()}: ').strip().lower()

    musica = []
    for _ in range(3):
        musica.append(input('Ingrese un género musical: ').strip().lower())
    
    print(f'Los hobbies de {nom.capitalize()} son: {musica}')
    agenda[nom]['hobbies'] = {'musica': musica}

def editar():
    nom = input('Ingrese el nombre de la persona a editar: ').strip().lower()
    if nom not in agenda:
        print(f'{nom.capitalize()} no está en la agenda.')
        return
    
    campo = input(f'Qué campo desea editar para {nom.capitalize()} (cc, tel, email, dir, job, hobbies): ').strip().lower()
    if campo not in agenda[nom]:
        print('Campo inválido.')
        return
    
    if campo == 'hobbies':
        agenda[nom]['hobbies']['musica'] = input('Ingrese los nuevos géneros musicales separados por coma: ').strip().lower().split(', ')
    else:
        nuevo_valor = input(f'Ingrese el nuevo valor para {campo}: ').strip().lower()
        agenda[nom][campo] = nuevo_valor

def consultar():
    nom = input('Ingrese el nombre de la persona a consultar: ').strip().lower()
    if nom not in agenda:
        print(f'{nom.capitalize()} no está en la agenda.')
        return
    
    print(f'-- {nom.capitalize()}:  {agenda[nom]}')

def menu():
    while True:
        print('\nMenú:')
        print('1. Imprimir la agenda')
        print('2. Agregar un contacto')
        print('3. Editar un contacto')
        print('4. Consultar un contacto')
        print('5. Salir')
        
        opcion = input('Seleccione una opción: ').strip()
        
        if opcion == '1':
            imprimir()
        elif opcion == '2':
            agregar()
        elif opcion == '3':
            editar()
        elif opcion == '4':
            consultar()
        elif opcion == '5':
            break
        else:
            print('Opción inválida.')

if __name__ == "__main__":
    menu()
