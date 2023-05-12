class Jugador:
    def __init__(self, nombre=None):
        self.nombre=nombre
        self.lista_fichas=[]
    
    #Juega la ficha y la elimina de la lista de fichas
    def jugar_ficha(self, ficha):
        self.lista_fichas.pop(ficha)
    #Pasa turno
    def pasar_turno(self):
        pass
