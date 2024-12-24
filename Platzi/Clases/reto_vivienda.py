# programa para construir una casa de vivienda de interes prioritario


class Vivienda():
    def __init__(self, ubicacion, credito, ahorros):
        self.ubicacion=ubicacion
        self.credito=credito
        self.ahorros=ahorros

    def solicitar_credito(self):
        pass

    @staticmethod
    def abonos_inteligentes(cuota1,cuota2):
        if cuota1.ahorros == cuota2.ahorros:
            print('Si es posible realizar abonos a capital')
        else:
            print('No es posible prepagar el crédito hipotecario')

def run():
    casa1=Vivienda('Turbaco', 136000000, 10000000)
    casa2=Vivienda('Turbaco',50000000, 10000000)
    Vivienda.abonos_inteligentes(casa1,casa2)

if __name__=='__main__':
    run()
