# programa que permite gestión de permisos de trabajo
print('')
def run():
    print('Menún principal para diligenciar los permisos de trabajo: ')
    print('')
    revisar()
 
def diligenciar():
    a=input('Introduzca el nombre del ejecutor: ')
    b=input('Introduzca el nombre del revisor: ')
    print(f'Las personas encargdas de diligenciar son: {a} y {b}')
    print('')

def revisar():
    a=input('Introduzca el nombre del revisor: ')
    b=input('Introduzca el nombre del revisor auxiliar: ')
    print(f'Las personas encargdas de diligenciar son: {a.capitalize()} y {b.capitalize()}')
    print('-'*50)

def aprovar():
    print('')



if __name__=='__main__':
    run()
