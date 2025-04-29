class Libro:
    def __init__(self, título, autor, ISBN, género, lista_de_préstamos):
        self.titulo = título
        self.autor = autor
        self.ISBN = ISBN
        self.genero = género
        self.lista_de_prestamos = lista_de_préstamos
        self.libros_registrados = []

    def mostrar_detalle(self):
        print("----- DETALLES DEL LIBRO -----")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.ISBN}")
        print(f"Género: {self.genero}")
        #print(f"Lista de Préstamos: {self.lista_de_prestamos}")
        print("----------------------------------\n")