class Character():
    def __init__(self, lista_personajes=[], lista_enemigos = [],lista_personajes_elegidos=[]):
        self.lista_personajes = lista_personajes
        self.lista_enemigos = lista_enemigos
        self.lista_personajes_elegidos = lista_personajes_elegidos

    def ShowPersonajes(self):
        for personaje in self.lista_personajes:
            personaje.View()
            print("")

    def ShowEnemigos(self):
        for enemigo in self.lista_enemigos:
            enemigo.View()
            print("")

    def Assign(self, personaje):
        personaje.lista_personajes.append(personaje)