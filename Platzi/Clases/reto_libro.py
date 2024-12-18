# Crea una clase Libro que tenga atributos para el título, el autor y el número de páginas. 
# Implementa un método para imprimir una descripción del libro y otro método para saber si el libro tiene más de 500 páginas.

class Libro:
    def __init__(self, titulo, autor, paginas, nobel=True):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        self.nobel=nobel

    def descripcion(self):
        print(f'El libro {self.titulo} del autor {self.autor} tiene {self.paginas}')
        print(f'{self.autor} fue ganador del nobel? {self.nobel} ')

    
def run():
    libro1=Libro('100 años De Soledad', 'Gabriel García Marquez', 520)
    libro1.descripcion()
    
    if libro1.paginas>400:
        print('Es un libro extenso para leer')
    else:
        print('Es un libro fácil de lerr')

    libro2=Libro('La Iliada', 'Homero', 250)
    libro2.descripcion()

    if libro2.paginas>400:
        print('Es un libro extenso para leer')
    else:
        print('Es un libro fácil de leer')
    

if __name__=='__main__':
    run()