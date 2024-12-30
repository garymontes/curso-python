# programa para construir una casa de vivienda de interes prioritario


class Vivienda():
    def __init__(self, ubicacion, credito, ahorros):
        self.ubicacion=ubicacion
        self.credito=credito
        self.ahorros=ahorros

    def solicitar_credito(self):
        pass

    def __str__(self):
        return (f'\nUbicación: {self.ubicacion}\nCrédito de: {self.credito}\nAhorros: {self.ahorros}')

    @staticmethod
    def abonos_inteligentes(cuota1,cuota2):
        if cuota1.ahorros == cuota2.ahorros:
            print('Si es posible realizar abonos a capital')
        else:
            print('No es posible prepagar el crédito hipotecario')

    @staticmethod
    def abonos_a_capital(abono1,abono2):
        if abono1.credito >= abono2.credito:
            print('Si es posible realizar abonos a para disminuir el crédito')
        else:
            print('No es posible realizar abonos al capital')

    @classmethod
    def estudio_credito(cls):
        u='Barranquilla'
        a=17
        b=90
        return cls(u,a,b)

def run():
    casa1=Vivienda('Turbaco', 136000000, 10000000)
    casa2=Vivienda('Turbaco',50000000, 10000000)
    Vivienda.abonos_inteligentes(casa1,casa2)
    print('-'*50)

    casa1=Vivienda('Turbaco', 36000000, 10000000)
    casa2=Vivienda('Turbaco',50000000, 5000000)
    Vivienda.abonos_a_capital(casa1,casa2)
    print('-'*50)
    print('-'*50)

    casa3=Vivienda.estudio_credito()
    print(f'El resultado de la casa 3 es: {casa3} ')
    







if __name__=='__main__':
    run()
