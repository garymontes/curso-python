
print('\n')
def agen():
    di={
        'Gary':{
            'Número':305,
            'Pais':'Col',
            'Código Postal':130013,
            'Dirección':'Santa Clara',
            'Pasa tiempos':['yuca','platano'],
            'Musica':{
                'Vallenato':'Ivan Villazon',
                'Reggae':'Bob Marley',
                'Salsa':'Niche'
            }
            
            },
        'Susana':{
            'Número':315,
            'Pais':'Mex',
            'Código Postal':130012,
            'Dirección':'Urb Santa Clara',
            'Pasa tiempos':['Cocina','Estudiar']
        },
        'Susy':{
            'Número':123,
            'Pais':'Usa',
            'Código Postal':2525,
            'Dirección':'Mz U lote 12',
            'Pasa tiempos':['Jugar','Tareas']
        },
        'Jesus':{
            'Número':310,
            'Pais':'Ven',
            'Código Postal':130010,
            'Dirección':'Consolata',
            'Pasa tiempos':['Trabajar','Correr'],
        },
        'Conchita':{
            'Número':311,
            'Pais':'Col',
            'Código Postal':130010,
            'Dirección':'Consolata',
            'Pasa tiempos':['Cocinar','Correr']
        }
    }
    
    
    for i,j in di.items():
        print(f'Los datos son: {i} - {j['Pais']} - {j['Código Postal']}')
        
    print('')
    
    a= di.items()
    for i,j in a:
        print(f'- {i} los datos son: {j['Número']}')
    
    print('-'*100)
    
    for i,j in di.items():
        if j['Pasa tiempos'][1]=='Estudiar':
            print(f'La busqueda encontró: {i}')
    print('-'*150)
    
    r=di['Gary']['Musica']
    for i in r:
        print(f'Los datos de Musica son: {i}-{r[i]}')
    print('-'*150)
    
    
    
    print('-'*150)
    
if __name__=='__main__':
    agen()
