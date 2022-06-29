class Cliente():
    def __init__(self, nombre, edad, direccion, lista_libros = []):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.lista_libros = []

    def View(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDirección: {self.direccion}")

    def ViewBooks(self):
        for libro in self.lista_libros:
            libro.View()
            print("")