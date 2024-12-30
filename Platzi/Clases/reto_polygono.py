

class Polygono():
    def __init__(self, num_lados, lados):
        self.num_lados = num_lados
        self.lados = lados


    def __str__(self):
        return f"Un poligono de {self.num_lados} lados y sus lados miden {self.lados}"

def run():
    a=int(input('Ingrese el número de lados del poligono: '))
    b=[int(input(f'Ingrese la longitud del lado {i+1} del poligono: ')) for i in range(a)]
    

    poligono = Polygono(a,b)
    print(poligono)

if __name__ == '__main__':
    run()