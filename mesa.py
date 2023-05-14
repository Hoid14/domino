from collections import deque
import random


class Mesa:
    def __init__(self,ficha_extremo1=None,ficha_extremo2=None, jugadores=None):
        self.fichas_iniciales=[]
        self.ficha_extremo1=ficha_extremo1
        self.ficha_extremo2=ficha_extremo2
        self.fichas_jugadas=[]
        self.jugadores=[]
        self.jugador_inicial=None
    
    
    
    def revolver_fichas(self):
        random.shuffle(self.fichas_iniciales)
    
    def repartir_fichas(self):
        self.fichas_iniciales=deque(self.fichas_iniciales)

        contador_jugador=0
        while(len(self.fichas_iniciales)!=0):
            ficha=self.fichas_iniciales.pop()

            if(contador_jugador==len(self.jugadores)):
                contador_jugador=0
            self.jugadores[contador_jugador].lista_fichas.append(ficha)
            if(ficha.numero_ficha==28):
                self.jugador_inicial=contador_jugador
            contador_jugador+=1

          


