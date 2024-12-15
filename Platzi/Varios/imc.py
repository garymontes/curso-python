# Programa que calcula el indice de masa corporal de la persona
def run():
    
    while True:
        try:
            peso=float(input('Ingrese su peso en kilo gramos: '))
            talla=float(input('Ingrese su estatura en metros: '))
            if peso<=0 or talla<=0:
                raise ZeroDivisionError('El peso y la estatura deben ser mayores a cero')
            imc= peso/talla**2
            clasificacion=clasificacion_imc(imc)
            return imc, clasificacion

        except ValueError: print('Ingresa datos validos, por favor continua con el proceso')
        except ZeroDivisionError as e: print(f'Error! {e}. por favor continua con el proceso')
            
       
def clasificacion_imc(imc):
    if imc < 18.5: return "Bajo peso" 
    elif 18.5 <= imc < 24.9: 
        return "Peso normal" 
    elif 25.0 <= imc < 29.9: 
        return "Sobrepeso" 
    elif 30.0 <= imc < 34.9: 
        return "Obesidad grado I" 
    elif 35.0 <= imc < 39.9: 
        return "Obesidad grado II" 
    else: 
        return "Obesidad grado III (obesidad mórbida)"


if __name__=='__main__':
    print('-'*30)
    resultado=run()
    
    if resultado is not None:
        imc,clasificacion=resultado
        #resultado=imc,clasificacion
        print(f'El indice de masa corporal es: {imc:.2f} y su clasifiación es: {clasificacion}')

    print('-'*30)



    