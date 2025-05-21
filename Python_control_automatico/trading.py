'''
Programa que calcula las ganancias en trading de criptomonedas en binance
'''
print('')
inversion=int(input('Ingrese la inversión inicial: '))
por_ganancia=float(input('Ingrese el porcentaje: '))
num_oper=int(input('Ingrese el número de operaciones: '))
profit= inversion
print('')

for i in range(num_oper):
   profit=profit*(por_ganancia/100)+profit
   print(f'En el profit {i+1} la ganancia será de: {profit:.2f}')
print('')
print(f'La inversión más ganancia será: {profit:.0f} dólares')
print('')
print(f'Al final la ganancia será: {(profit-inversion):.0f} dólares.')
print(f'El porcentaje de ganancia fue: {(num_oper*(por_ganancia/100)*100):.0f} %')
print('')


 

    
