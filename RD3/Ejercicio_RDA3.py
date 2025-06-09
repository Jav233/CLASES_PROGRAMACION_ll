# Crea una lista vacía llamada historial
historial = []

# Mostrar el historial vacío
#print("Historial:", historial)

while True:
    print("*************************************************************")
    print("\n-------Bienvenido al sistema de gestión de historial------\n")
    print("*************************************************************\n")
    print("1. Mostrar historial vacio")
    print("2. Agregar una tarea al historial")
    print("3. Mostrar pagina actual del historial")
    print("4. Eliminar la última tarea del historial")
    print("5. Verificar el historial")
    print("6. Salir del programa\n")
    print("*************************************************************")
    
    opcion = int(input("Seleccione una opción (1-6): "))
    while opcion < 1 or opcion > 6:
        print("Opción inválida. Por favor, seleccione una opción entre 1 y 6.")
        opcion = int(input("Seleccione una opción (1-6): "))
    
    if opcion == 1:
        #print("Mostrar historial vacío")
        if not historial:
            print("El historial está vacío.")
        else:
            print("Historial:", historial) 
    elif opcion == 2:
        
        print("Agregar una tarea al historial")
        historial.append("www.google.com")
        historial.append("www.python.org")
        historial.append("www.stackoverflow.com")
        cont = 0
        for pagina in historial:
            cont += 1
            print(f"Historia {cont}:", pagina)
        #print("Tareas agregadas al historial:", historial)
        
        print("///////Tareas agregadas al historial de manera correcta.////////")
        
    elif opcion == 3:
        
        if historial:
            
            print("Página actual del historial:", historial[-1])
        else:
            print("El historial está vacío.")
            
    elif opcion == 4:
        
        if historial:
            tarea_eliminada = historial.pop()
            print("Volviste desde:", tarea_eliminada)
            print("Última tarea eliminada del historial:", tarea_eliminada)
        else:
            print("No hay tareas para eliminar del historial.")
            
    elif opcion == 5:
        
        print("El historial contiene las siguientes páginas:")
        if len(historial) > 0:
            for pagina in historial:
                print(pagina)
        else:
            print("El historial está vacío.")
    elif opcion == 6:
        print("Gracias por utilizar el sistema de gestión de historial. Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 6.")
    print()  # Línea en blanco para mejorar la legibilidad
    

        
    