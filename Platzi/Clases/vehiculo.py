


class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.marca=marca
        self.modelo=modelo
        self.año=año

    def __str__(self):
        return f'Marca:{self.marca}, Modelo:{self.modelo}, Año:{self.año}'

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_de_puertas):
        super().__init__(marca, modelo, año)
        self.numero_de_puertas=numero_de_puertas
    
    def __str__(self):
        return f'{super().__str__()} y tiene {self.numero_de_puertas} puertas'

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, placa):
        super().__init__(marca, modelo, año)
        self.placa=placa
    
    def __str__(self):
        return f'{super().__str__()} y número de placa:{self.placa}'

class Mulita(Vehiculo):
    def __init__(self, marca, modelo, año, puestos):
        super().__init__(marca, modelo, año)
        self.puestos=puestos
        
    def __str__(self):
        return f'{super().__str__()} y tiene {self.puestos} puestos'
    
    

car=Auto('Ford', 'Mustang', 2025, 4)
print(car.__str__())
print()

mot=Moto('Yamaha', 'XTZ', 2024, 2015)
print(mot.__str__())

mul=Mulita('Eco','Lento',2000, 4 )
print(mul.__str__())