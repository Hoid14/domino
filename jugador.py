class Jugador:
    def __init__(self, nombre=None):
        self.nombre=nombre
        self.lista_fichas=[]
    
    #Juega la ficha y la elimina de la lista de fichas
    def jugar_ficha(self, ficha_extremo1,ficha_extremo2):
        
        ficha_seleccionada=None
        while True:
            print("----------------------------------------------------------------------------")
            print("TU TURNO")
            #Mostrar los extremos actuales del domino
            print(f"Extremo 1: {ficha_extremo1} | Extremo 2: {ficha_extremo2}")
            #Mostrar las fichas al usuario
            print("Selccione una ficha:")
            for i, ficha in enumerate(self.lista_fichas):
                print(f"Opcion {i+1}: {ficha.lado1} | {ficha.lado2}")
            print(f"Opcion {len(self.lista_fichas)+1}: Pasar turno")
            #Solicitar al usuario que ingrese el indice de la ficha deseada
            opcion=input("Ingrese el numero de la ficha seleccionada: ")

            try: 
                opcion=int(opcion)
                if opcion>=1 and opcion <= len(self.lista_fichas)+1:
                    if opcion==len(self.lista_fichas)+1:
                        return None
                    ficha_seleccionada=self.lista_fichas[opcion-1]
                
                    #Verificar si la ficha cumple con la condicion deseada
                    if ficha_seleccionada.lado1==ficha_extremo1 or ficha_seleccionada.lado1==ficha_extremo2 or ficha_seleccionada.lado2==ficha_extremo1 or ficha_seleccionada.lado2==ficha_extremo2:
                        return self.lista_fichas.pop(opcion-1)
                    
                    else:
                        raise ValueError
                
                else:
                    raise ValueError
            except ValueError:
                print("Entrada invalida, intente nuevamente")

                      
        
        
    
