# Programa que almacena información de estudiantes de un colegio, nombre, apellidos, edad, sexo y grado, utilizando diccionarios
print('\n')

def estudiantes():
    datos={
        'Nombre y Apellidos':['Gary Montes','Susana Montes','Susana Olier','Consuelo Bracamonte','Jesús Montes','Nicasia Paternina','Francisco Montes','Antonia Meza'],
        'Edad': [41,10,38,65,71,94,97,96],
        'Sexo':['M','F','F','F','M','F','M','F'],
        'Grado':[1,2,3,4,5,6,7,8]            
    }
    
    for i in datos:
        print(f'{i} {datos[i]}')
        
    print('-'*50)
    
    for i,j in datos.items():
        print(f'{i},{j}')
    
    print('-'*50)

def est():
    datos={
        'Nombre y Apellidos':['Gary Montes','Susana Montes','Susana Olier','Consuelo Bracamonte','Jesús Montes','Nicasia Paternina','Francisco Montes','Antonia Meza'],
        'Edad': [41,10,38,65,71,94,97,96],
        'Sexo':['M','F','F','F','M','F','M','F'],
        'Grado':[1,2,3,4,5,6,7,8]            
    }
    for i in datos:
        for j in datos.values():
            print(f' - {j}')
        print('-'*50)
 
 
 
if __name__=='__main__':
    pass
    
print('\n')