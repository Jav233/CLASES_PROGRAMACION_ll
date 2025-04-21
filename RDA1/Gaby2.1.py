while True:
    print("------------------------------------------------------------------------------------------------------")
    print("Bienvenido al programa de selección de jugadores para la Copa Mundial de Fútbol")
    print("Por favor, ingresa los puntajes de los jugadores y su estado de salud.")
    print("El programa calculará el puntaje total de cada jugador y determinará si es apto para la selección.")
    print("Si el puntaje es menor a 70, el jugador no entra a la selección.")
    print("Si el puntaje está entre 70 y 80, el jugador va a repechaje.")
    print("Si el puntaje está entre 80 y 90, el jugador pasa directo a la selección y debe elegir una región.")
    print("Si el puntaje es mayor a 90, el jugador pasa directo a la selección sin elegir región.")
    print("------------------------------------------------------------------------------------------------------")

    cantidad = int(input("¿Cuántos jugadores deseas ingresar?: "))
    while cantidad <= 0:
        print("La cantidad debe ser mayor a cero.")
        cantidad = int(input("¿Cuántos jugadores deseas ingresar?: "))

    seleccionados_total = 0
    repechaje_total = 0
    no_seleccionados_total = 0
    lesionados_count = 0

    puntajes_europeo_total = 0
    puntajes_asiatica_total = 0
    puntajes_americano_total = 0
    
    jugadores_europeos = 0
    jugadores_asiaticos = 0
    jugadores_americanos = 0

    for num_jugador in range(1, cantidad + 1):
        print("------------------------------------------------------------------------------------------------------")
        print(f"Jugador {num_jugador}:")
        
        puntaje = int(input("Ingresa el puntaje del jugador: "))
        while puntaje < 0 or puntaje > 100:
            print("El puntaje debe estar entre 0 y 100.")
            puntaje = int(input("Ingresa el puntaje del jugador: "))
        
            

        if puntaje < 0 or puntaje > 100:
            print("El puntaje debe estar entre 0 y 100.")
            continue

        texto_jugador = f"Jugador {num_jugador} ::::::: "

        if puntaje < 70:
            texto_jugador += "No entra a la selección."
            no_seleccionados_total += 1

        elif 70 <= puntaje < 80:
            texto_jugador += "Va a repechaje."
            repechaje_total += 1
            salud = input("¿El jugador está lesionado? (s/n): ").lower()
            if salud == 's':
                lesionados_count += 1
                print("→ Jugador lesionado. No puede participar.")
                continue

        elif 80 <= puntaje <= 90:
            print("→ Pasa directo. Debe elegir una región:")
            print("  1: Europeo")
            print("  2: Asiática")
            print("  3: Americana")
            seleccion = int(input("Elige una opción (1-3): "))
            while seleccion <=0 or seleccion > 3:
                print("Opción inválida. Intenta de nuevo.")
                seleccion = int(input("Elige una opción (1-3): "))

            if seleccion == 1:
                puntajes_europeo_total += puntaje
                texto_jugador += "Pasa directo (Europeo)"
                jugadores_europeos += 1
            elif seleccion == 2:
                puntajes_asiatica_total += puntaje
                texto_jugador += "Pasa directo (Asiática)"
                jugadores_asiaticos += 1
            elif seleccion == 3:
                puntajes_americano_total -= puntaje  # Se resta el puntaje
                jugadores_americanos += 1
                texto_jugador += "Pasa directo (Americana, puntaje restado)"

            seleccionados_total += 1

        elif puntaje > 90:
            texto_jugador += "Pasa directo sin elegir región."
            seleccionados_total += 1

        print(texto_jugador)
    puntaje_total_general = puntajes_europeo_total + puntajes_asiatica_total + puntajes_americano_total
    
    porcentaje_lesionados = (lesionados_count / cantidad) * 100
    porcentaje_europeos = (jugadores_europeos / cantidad) * 100
    porcentaje_asiaticos = (jugadores_asiaticos / cantidad) * 100
    porcentaje_americanos = (jugadores_americanos / cantidad) * 100
    
    porcentaje_repechaje = (repechaje_total / cantidad) * 100
    porcentaje_no_seleccionados = (no_seleccionados_total / cantidad) * 100
    
    print("------------------------------------------------------------------------------------------------------")
    print("Resumen final:")
    print(f"Total de jugadores ingresados: {cantidad}")
    print(f"Lesionados: {lesionados_count} → {porcentaje_lesionados:.2f}%")
    print(f"Seleccionados directamente: {seleccionados_total}")
    print(f"  - Europeos: {jugadores_europeos} → {porcentaje_europeos:.2f}%")
    print(f"  - Asiáticos: {jugadores_asiaticos} → {porcentaje_asiaticos:.2f}%")
    print(f"  - Americanos: {jugadores_americanos} → {porcentaje_americanos:.2f}%")
    print(f"En repechaje: {repechaje_total}")
    print(f"No seleccionados: {no_seleccionados_total}")
    print("Puntajes por región:")
    print(f"  Europeo: {puntajes_europeo_total}")
    print(f"  Asiática: {puntajes_asiatica_total}")
    print(f"  Americana (restados): {puntajes_americano_total}")
    print(f"→ Puntaje total final: {puntaje_total_general}")
    print(f"En repechaje: {repechaje_total} → {porcentaje_repechaje:.2f}%")
    print(f"No seleccionados: {no_seleccionados_total} → {porcentaje_no_seleccionados:.2f}%")
    print("------------------------------------------------------------------------------------------------------")

    continuar = input("¿Deseas ingresar otra tanda de jugadores? (s/n): ").lower()
    if continuar != 's':
        print("Gracias por usar el programa. ¡Hasta la próxima!")
        break

                


