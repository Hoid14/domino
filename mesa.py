import random

class Mesa:
    def __init__(self,ficha_extremo1=None,ficha_extremo2=None, jugadores=None):
        self.fichas_iniciales=[]
        self.ficha_extremo1=ficha_extremo1
        self.ficha_extremo2=ficha_extremo2
        self.fichas_jugadas=[]
        self.jugadores=[]
    
    def revolver_fichas(self):
        random.shuffle(self.fichas_iniciales)


