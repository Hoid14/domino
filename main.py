

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
        player.nombre="Humano" #Este sera el jugador que nosotros controlemos
    else:
        player.nombre="Maquina "+str(i) #Los demas seran maquinas
    mesa.jugadores.append(player)
""""
muestra fichas de domino
for i in mesa.fichas_iniciales:
    print(i.numero_ficha," - ",i.lado1," - ",i.lado2)

for i in mesa.jugadores[mesa.jugador_inicial].lista_fichas:
    print(i.numero_ficha," - ",i.lado1," - ",i.lado2)

print(len(mesa.jugadores[jugador_actual].lista_fichas))
"""

#Revolver fichas
mesa.revolver_fichas()

#Repartir fichas
mesa.repartir_fichas()


#Inicio del juego

#Este es el primer turno, donde se pone el doble 6 y se pasa turno
jugador_actual=mesa.jugador_inicial #Designamos al jugador actual que comenzara la partida con el doble 6

for i in mesa.jugadores[jugador_actual].lista_fichas:
    if(i.numero_ficha==28):
        indice=mesa.jugadores[jugador_actual].lista_fichas.index(i)
        ficha_jugada=mesa.jugadores[jugador_actual].lista_fichas.pop(indice)#Eliminamos la ficha jugada de su lista de fichas
        
mesa.fichas_jugadas.append(ficha_jugada) #Agregamos la ficha jugada a la lista de fichas jugadas de mesa

mesa.ficha_extremo1=ficha_jugada.lado1 #Establecemos el extremo 1
mesa.ficha_extremo2=ficha_jugada.lado2 #Establecemos el extremo 2

print(jugador_actual)
if (jugador_actual==len(mesa.jugadores)-1):
    jugador_actual=0

jugador_actual+=1

while True:
    if mesa.jugadores[jugador_actual].nombre=="Humano": #Esta es la jugada del humano
        pass
    else: #Esta es la jugada de la maquina
        resultado=[mesa.jugadores[jugador_actual].lista_fichas.index(ficha) for ficha in mesa.jugadores[jugador_actual].lista_fichas if ficha.lado1==mesa.ficha_extremo1 or ficha.lado1==mesa.ficha_extremo2 or ficha.lado2==mesa.ficha_extremo1 or ficha.lado2==mesa.ficha_extremo2] #Buscamos en la lista de fichas de la maquina, si el lado 1 de sus fichas coincide con alguno de los extremos
        
        print("Fichas de la maquina")
        for i in mesa.jugadores[jugador_actual].lista_fichas:
            print(i.lado1," - ",i.lado2) 

        print()
        print(len(resultado))
        if len(resultado)>0:
            ficha_jugada=mesa.jugadores[jugador_actual].lista_fichas.pop(resultado[0]) #Eliminamos la ficha jugada de su lista de fichas
            mesa.fichas_jugadas.append(ficha_jugada)#Agregamos la ficha jugada a la lista de fichas jugadas de mesa

            #Actualizamos los extremos
            mesa.ficha_extremo1=ficha_jugada.lado1 #Establecemos el extremo 1
            mesa.ficha_extremo2=ficha_jugada.lado2 #Establecemos el extremo 2

    
    a=input()
    jugador_actual+=1   
    if jugador_actual==len(mesa.jugadores): 
        jugador_actual=0
    
    
    



    



    





