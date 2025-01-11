'''
Sobreescritura de Métodos
Crea una clase base CuentaBancaria con métodos para depositar y retirar dinero, y obtener el saldo actual. 
Luego, crea una clase derivada CuentaAhorro que tenga un método adicional para calcular los intereses.
'''
class CuentaBancaria():
    
    def __init__(self, banco, cuenta_bancaria, titular_cuenta, saldo):
        self.banco=banco
        self.cuenta_bancaria=cuenta_bancaria
        self.titular_cuenta=titular_cuenta
        self.saldo=saldo
    
    def __str__(self):
        return (f'Nombre: {self.titular_cuenta}, Entidad Bancaria: {self.banco}, # cuenta: {self.cuenta_bancaria}')

    def depositar (self, dinero_depositar):
        if dinero_depositar>0:
            self.saldo+=dinero_depositar

        return (f'se depositaron {dinero_depositar} y el nuevo saldo es: {self.saldo} pesos colombianos')

    def retirar_dinero (self):
        pass

    def obtener_saldo (self):
        pass

class CuentaAhorro(CuentaBancaria):
    
    def __init__(self):
        super().__init__()
    
    def calcular_interes(self):
        pass

    
deposito1=CuentaBancaria('Bancolombia', '67858063954', 'Gary Montes',100)

print(deposito1.depositar(1000))
print(deposito1.__str__())