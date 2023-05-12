from fichas import Ficha
from jugador import Jugador
from mesa import Mesa
#Generar mesa
mesa=Mesa()

#Generar todas las fichas del juego y las guarda en fichas_iniciales de la mesa
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
    ficha=Ficha(lado1,lado2)
    contador+=1
    cantidad_fichas-=1
    lado2+=1
    mesa.fichas_iniciales.append(ficha)
#Generar jugadores
for i in range(4):
    player=Jugador()
    if(i==0):
        player.nombre="Humano"
    else:
        player.nombre="Maquina "+str(i)
    mesa.jugadores.append(player)

for i in mesa.jugadores:
    print(i.nombre)

#Repartir fichas



    





