print("------------------------------------------------------------------------------------------------------")
print("Bienvenido al programa de selección de jugadores para la Copa Mundial de Fútbol")
print("Por favor, ingresa los puntajes de los jugadores y su estado de salud.")
print("El programa calculará el puntaje total de cada jugador y determinará si es apto para la selección.")
print("Si el puntaje es menor a 70, el jugador no entra a la selección.")
print("Si el puntaje está entre 70 y 80, el jugador va a repechaje.")
print("Si el puntaje está entre 80 y 90, el jugador pasa directo a la selección y debe elegir una región.")
print("Si el puntaje es mayor a 90, el jugador pasa directo a la selección sin elegir región.")
print("------------------------------------------------------------------------------------------------------")
print("Por favor, ingresa la cantidad de jugadores que deseas evaluar.")
cantidad = int(input("¿Cuántos jugadores deseas ingresar?: "))

jugador_numero = 1  
puntajes_europeo = 0
puntajes_asiatica = 0
puntajes_latina = 0
lesionados_count = 0
repechaje_total = 0

while jugador_numero <= cantidad:
    puntaje = int(input("Ingresa el puntaje del jugador " + str(jugador_numero) + ": "))
    texto_jugador = "Jugador " + str(jugador_numero) + " ::::::: "

    if puntaje < 0 or puntaje > 100:
        print("→ No entra (puntaje inválido)")
        texto_jugador += "Puntaje inválido"
    else:
        if 80 <= puntaje <= 90:
            print("→ Pasa directo")
            print("  - Debe elegir una región")

            print("    Opción 1: Europeo")
            print("    Opción 2: Asiática")
            print("    Opción 3: Latina")

            seleccion = int(input("Elige una opción (1-3): "))

            while seleccion not in [1, 2, 3]:  # Validar que la opción esté entre 1 y 3
                print(" Opción inválida, por favor elige una opción válida.")
                seleccion = int(input("Elige una opción (1-3): "))

            if seleccion == 1:
                puntajes_europeo += puntaje
                print("Seleccionó: Europeo")
                texto_jugador += "Pasa directo (Europeo)"
            elif seleccion == 2:
                puntajes_asiatica += puntaje
                print("Seleccionó: Asiática")
                texto_jugador += "Pasa directo (Asiática)"
            elif seleccion == 3:
                puntajes_latina += puntaje
                print("Seleccionó: Latina")
                texto_jugador += "Pasa directo (Latina)"

        elif puntaje >= 70:
            print(" Va a repechaje")
            repechaje_total += 1
            lesionado = input("¿Está lesionado? (sí/no): ").lower()
            if lesionado == "sí":
                lesionados_count += 1
                texto_jugador += "Va a repechaje (lesionado)"
            else:
                texto_jugador += "Va a repechaje (No lesionado)"
        else:
            print(" No entra a la selección")
            texto_jugador += "No entra a la selección"