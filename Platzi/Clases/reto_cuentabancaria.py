# Crea una clase CuentaBancaria que tenga atributos para el número de cuenta y el saldo. Implementa métodos para depositar, retirar y consultar el saldo, 
# y asegúrate de manejar los posibles errores, como intentar retirar más dinero del que hay disponible.


class CuentaBancaria:
    def __init__(self, num_cuenta, saldo=0):
        self.num_cuenta=num_cuenta
        self.saldo=saldo

    def depositar(self,cantidad=1000):
        self.saldo+=cantidad
        print(f'Se hizo un deposito a la cuenta #: {self.num_cuenta}. El nuevo saldo es: {self.saldo}')

    def retirar(self,cantidad=80):
        if cantidad>self.saldo:
            print(f'Fondos insuficientes.')
        else:
            self.saldo-=cantidad
            print(f'Se acaba de hacer un retiro por valor de {cantidad} el nuevo saldo es: {self.saldo}')

    def consultar_saldo(self):
        print(f'**CONSULTA DE SALDO** El saldo actual es {self.saldo}')


def operaciones():
    a=int(input('Ingrese el valor inicial para la consignación: '))
    b=int(input('Ingrese el valor para el retiro: '))
    
    oper1=CuentaBancaria('67858063954',a)
    oper2=CuentaBancaria('6785063954', b)
   
    oper1.depositar()
    oper1.retirar()
    oper1.consultar_saldo()

    oper2.depositar()
    oper2.retirar()
    oper2.consultar_saldo()

if __name__=='__main__':
    print('')
    operaciones()
    print('-'*50)
