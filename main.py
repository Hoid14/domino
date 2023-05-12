from fichas import Ficha
from jugador import Jugador

#Genera todas las fichas del juego y las guarda en l
l=[] #Las guarda aqui
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
    l.append(ficha)

for i in l:
    print(i.lado1," - ",i.lado2)

#Generar jugadores



