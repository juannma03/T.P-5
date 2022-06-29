class Biblioteca():
    def __init__(self, lista_libros = [], lista_clientes = []):
        self.lista_libros = lista_libros
        self.lista_clientes = lista_clientes

    def ShowBooks(self):
        for libro in self.lista_libros:
            libro.View()
            print("")

    def ShowClients(self):
        for client in self.lista_clientes:
            client.View()
            print("")

    def Assign(self, libro, cliente):
        cliente.lista_libros.append(libro)