print("--------------------------------------------------------------")
print("Bienvenido al programa de clasificación para el Mundial")
print("--------------------------------------------------------------")

puntos_total=0
puntos=int(input("Ingrese sus puntos: "))
if puntos <= 0: #puntaje invalido
    print("puntaje no valido")

else:
    print("Su puntaje es valido")
    print("--------------------------------------------------------------")
    print("Clasificacion de jugadores")
    print("--------------------------------------------------------------")
    
    if puntos > 25:
        print("Clasifica directamente al mundial.... Felicidades")
        print(f"Su puntaje es: {puntos} puntos")
    elif puntos >=20 and puntos <= 25:
        print("Clasifica al repechaje")
        print(f"Su puntaje es: {puntos} puntos")
        jugadores_europa=0
        pregunta = input("¿Tiene en Europa jugadores? (si/no): ").lower()
        if pregunta == "si":
            europa = int(input("Cuantos jugadores tiene jugando en Europa: "))
            if europa >= 1:
                precios = 0
                for i in range(1, europa + 1):
                    precio = float(input(f"Ingrese el precio del jugador {i} en millones de dolares: "))
                    precios += precio
                if precios > 10:
                    print("Refuerzo bueno")
                    puntos_total = puntos + 2
                    print(f"Su puntaje total es: {puntos_total} puntos")
                    if puntos_total >= 30:
                        print("Clasifica directamente al mundial")
                        print(f"Su puntaje total es: {puntos_total} puntos")
                    else:
                        print("Clasifica al repechaje. No le alcanza para clasificar directamente")
                        print(f"Su puntaje total es: {puntos_total} puntos")
                elif precios < 10:
                    print("Refuerzo regular")
                    puntos_total = puntos + 1
                    print(f"Su puntaje total es: {puntos_total} puntos")
                    if puntos_total >= 30:
                        print("Clasifica directamente al mundial")
                        print(f"Su puntaje total es: {puntos_total} puntos")
                    else:
                        print("Clasifica al repechaje. No le alcanza para clasificar directamente")
                        print(f"Su puntaje total es: {puntos_total} puntos")
        else:
            print("No tiene jugadores en Europa")
            puntos_total = puntos + 0
            print(f"Su puntaje total es: {puntos_total} puntos")
            print("Clasifica al repechaje. No le alcanza para clasificar directamente")
                
    elif puntos < 20:
        print("No clasifica. Queda Eliminado")
        print(f"Su puntaje es: {puntos} puntos")
        lesionados = 0
        pregunta = input("¿Tiene jugadores lesionados? (si/no): ").lower()
        if pregunta == "si":
            lesionados = int(input("Cuantos jugadores tiene lesionados: "))
            if lesionados >= 2 or lesionados <= 3:
                puntos_total = puntos + 2
                print(f"Su puntaje total es: {puntos_total} puntos")
                if puntos_total >= 30:
                    print("Clasifica directamente al mundial")
                    print(f"Su puntaje total es: {puntos_total} puntos")
                else:
                    print("Clasifica al repechaje. No le alcanza para clasificar directamente")
                    print(f"Su puntaje total es: {puntos_total} puntos")
            elif lesionados == 1:
                puntos_total = puntos + 1
                print(f"Su puntaje total es: {puntos_total} puntos")
                if puntos_total >= 30:
                    print("Clasifica directamente al mundial")
                    print(f"Su puntaje total es: {puntos_total} puntos")
                else:
                    print("Clasifica al repechaje. No le alcanza para clasificar directamente")
                    print(f"Su puntaje total es: {puntos_total} puntos")
            elif lesionados == 0:
                puntos_total = puntos + 0
                print(f"Su puntaje total es: {puntos_total} puntos")
        else:
            print("No tiene jugadores lesionados")
            puntos_total = puntos + 0
            print(f"Su puntaje total es: {puntos_total} puntos")
            print("No clasifica. Queda Eliminado")
            
                    
        print("--------------------------------------------------------------")
        
    

# elif puntos < 20: 
#   #europa jugadores proceso for
#   euro=0
#   euro=int(input("Total de jugadores en europa : "))
#   for i in range(1,euro+1):
#     a=int(input("Ingrese el precio de su jugador(en milones): "))
#   total=0
#   total +=a
#   print("El total de valor es :",total,"millones")
#   #asia jugadoresp proceso for
#   asia=0
#   asia=int(input("Total de jugadores en asia : "))

#   for i in range(1,asia+1):
#     b=int(input("Ingrese el precio de su jugador(en milones): "))
#   total2=0
#   total2 +=b
#   print("El total de valor es :",total2,"millones")

#   #latin jugadores proceso for
#   latin=0
#   latin=int(input("Total de jugadores en latinoamerica : "))
#   for i in range(1,latin+1):
#     c=int(input("Ingrese el precio de su jugador(en milones): "))
#   total3=0
#   total3 +=c
#   print("El total de valor es :",total3,"millones")

#   total=total+total2+total3
#   print("El total del valor de sus jugadores es :",total,"millones")