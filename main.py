

from fichas import Ficha
from jugador import Jugador
from mesa import Mesa
#Generar mesa
mesa=Mesa()

#Generar todas las fichas del juego y las guarda en fichas_iniciales de la mesa
numero=1
cantidad_fichas=28
contador_final=7
contador=0
lado1=0
contador2=0
lado2=0
while(cantidad_fichas!=0):
    if(contador==contador_final):
        contador_final-=1
        lado1+=1
        contador=0
        contador2+=1
        lado2=contador2

    ficha=Ficha(numero,lado1,lado2)
    numero+=1
    contador+=1
    cantidad_fichas-=1
    lado2+=1
    mesa.fichas_iniciales.append(ficha)
#Generar  y guardarlos en la lista mesa.jugadores
for i in range(4):
    player=Jugador()
    if(i==0):
        player.nombre="Humano"
    else:
        player.nombre="Maquina "+str(i)
    mesa.jugadores.append(player)
""""
muestra fichas de domino
for i in mesa.fichas_iniciales:
    print(i.numero_ficha," - ",i.lado1," - ",i.lado2)

for i in mesa.jugadores[mesa.jugador_inicial].lista_fichas:
    print(i.numero_ficha," - ",i.lado1," - ",i.lado2)
"""

#Revolver fichas
mesa.revolver_fichas()

#Repartir fichas
mesa.repartir_fichas()


#Inicio del juego



    



    





