


class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo=titulo
        self.autor=autor
        self.año=año

    def __str__(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año}'

class Libreria:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'Libro "{libro.titulo}" agregado a la librería.')

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f'Libro "{titulo}" eliminado de la librería.')
                return
        print(f'Libro "{titulo}" no encontrado en la librería.')

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def mostrar_libros(self):
        if not self.libros:
            print('La librería está vacía.')
        else:
            print('Libros en la librería:')
            for libro in self.libros:
                print(libro)

# Crear instancias de la clase Libro
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 1967)
libro2 = Libro('El amor en los tiempos del cólera', 'Gabriel García Márquez', 1985)
libro3 = Libro('Crónica de una muerte anunciada', 'Gabriel García Márquez', 1981)

# Crear instancia de la clase Libreria y agregar libros
mi_libreria = Libreria()
mi_libreria.agregar_libro(libro1)
mi_libreria.agregar_libro(libro2)
mi_libreria.agregar_libro(libro3)

# Mostrar todos los libros en la librería
mi_libreria.mostrar_libros()

# Buscar un libro en la librería
libro_encontrado = mi_libreria.buscar_libro('El amor en los tiempos del cólera')
if libro_encontrado:
    print(f'Libro encontrado: {libro_encontrado}')
else:
    print('Libro no encontrado.')

# Eliminar un libro de la librería
mi_libreria.eliminar_libro('Cien años de soledad')
mi_libreria.mostrar_libros()



