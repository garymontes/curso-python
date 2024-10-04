


def cdt_lulo():
    # Programa que calcula los intereses que genera la renta de 10 millones de pesos a una Tasa E.A de 13%
    tasa_Mensual = 0.0108
    print('')
    print(f'La tasa de Lulo Bank es de un 13% efectivo anual y un {tasa_Mensual*100}% efectivo mensual')
    print('')
    
    inv_inicial=int(input('Ingrese un valor para la inversión: '))
    f=inv_inicial*1
    print(f'El id de inv_inicial es: {id(inv_inicial)}')
    print(f'El id de f es: {id(f)}')
    abonos=int(input('Ingrese un abono fijo mensual: '))
    
    
    print(f'La inversión inicial en Lulo Bank será de: {inv_inicial:,} millones COP')
    print('')
    
    for i in range(1,49):
        ic=inv_inicial*tasa_Mensual
        g=ic+inv_inicial+abonos*tasa_Mensual+abonos
        print(f'Intereses del mes: {i} seran de: {ic:,.0f} total: {g:,.0f}')
        inv_inicial=g
    print('')
    print(f'Los interes totales ganados en {i} meses serian: {g-f:,.0f}')
    print('')
        
    
        
        
        
        
       
        
    
    print('')






if __name__=='__main__':
    cdt_lulo()


    
