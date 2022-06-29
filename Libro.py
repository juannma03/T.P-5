class Libro():
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def View(self):
        print(f"Titulo: {self.titulo}\nAutor: {self.autor}\nPrecio: {self.precio}")