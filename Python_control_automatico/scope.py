def externa():
    mensaje = "Soy una variable en el ámbito enclosing"

    def interna():
        print(mensaje)  # ¿Podrá acceder a la variable de la función externa?

    interna()

externa()