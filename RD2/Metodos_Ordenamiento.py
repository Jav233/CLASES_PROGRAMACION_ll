#Metodos de Ordenamiento
# * Bubble Sort
# * Insertion Sort
# * Selection Sort
# Añada contadores que muestren:
#     * Número de comparaciones realizadas.
#     * Número de intercambios efectuados.

# print("-------------------------------")
# print("Metodos de Ordenamiento")
# print("Bubble Sort")
# print("-------------------------------")
precios_varios = [5.99, 3.49, 2.99, 4.99, 1.99, 6.49, 3.99, 2.49, 4.49, 1.49]
# * Bubble Sort
def bubble_sort(precios_varios):
    comparaciones = 0   
    intercambios = 0
    n = len(precios_varios)
    # Recorremos toda la lista n veces
    for i in range(n):
        # En cada pasada, comparamos elementos adyacentes
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            comparaciones += 1
            if precios_varios[j] > precios_varios[j+1]:
                precios_varios[j], precios_varios[j+1] = precios_varios[j+1], precios_varios[j]
                # Intercambio usando desempaquetado de tuplas
                intercambios += 1
    return precios_varios, comparaciones, intercambios

# print("Lista original de precios:", precios_varios)
# sorted_bubble, comparaciones_bubble, intercambios_bubble = bubble_sort(precios_varios.copy())
# print("Lista ordenada con Bubble Sort:", sorted_bubble)
# print("Comparaciones realizadas:", comparaciones_bubble)
# print("Intercambios realizados:", intercambios_bubble)

# print("-------------------------------")
# print("Metodos de Ordenamiento")
# print("Insercion Sort")
# print("-------------------------------")
# * Insertion Sort
def insertion_sort(precios_varios):
    comparaciones = 0
    intercambios = 0
    # Recorremos desde el segundo elemento hasta el final de la lista
    for i in range(1, len(precios_varios)):
        key = precios_varios[i]
        j = i - 1
        # Mover los elementos mayores que key a una posición adelante
        while j >= 0 and key < precios_varios[j]:
            comparaciones += 1
            precios_varios[j + 1] = precios_varios[j]
            j -= 1
            intercambios += 1
        precios_varios[j + 1] = key
        intercambios += 1 if j != i - 1 else 0  # Solo cuenta el intercambio si realmente se movió el elemento
    return precios_varios, comparaciones, intercambios

# print("Lista original de precios:", precios_varios)
# sorted_insertion, comparaciones_insertion, intercambios_insertion = insertion_sort(precios_varios.copy())
# print("Lista ordenada con Insertion Sort:", sorted_insertion)
# print("Comparaciones realizadas:", comparaciones_insertion)
# print("Intercambios realizados:", intercambios_insertion)

# * Selection Sort
# print("-------------------------------")
# print("Metodos de Ordenamiento")
# print("Selection Sort")
# print("-------------------------------")

def selection_sort(precios_varios):
    comparaciones = 0
    intercambios = 0
    n = len(precios_varios)
    # Recorremos toda la lista
    for i in range(n):
        # Buscamos el elemento más pequeño en el resto de la lista
        min_index = i
        for j in range(i + 1, n):
            comparaciones += 1
            if precios_varios[j] < precios_varios[min_index]:
                min_index = j
        # Intercambiamos el elemento encontrado con el primer elemento
        if min_index != i:
            precios_varios[i], precios_varios[min_index] = precios_varios[min_index], precios_varios[i]
            intercambios += 1
    return precios_varios, comparaciones, intercambios

# print("Lista original de precios:", precios_varios)
# sorted_selection, comparaciones_selection, intercambios_selection = selection_sort(precios_varios.copy())
# print("Lista ordenada con Selection Sort:", sorted_selection)
# print("Comparaciones realizadas:", comparaciones_selection)
# print("Intercambios realizados:", intercambios_selection)

listas_prueba = {
    "Ascendente": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Descendente": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    "Aleatorio": [5, 2, 8, 1, 9, 4, 6, 3, 7, 10]
}

def mostrar_resultados(nombre_algoritmo, funcion_ordenamiento):
    # Imprime el nombre del algoritmo de ordenamiento que se va a evaluar
    print(f"\n--- {nombre_algoritmo} ---")
    # Recorre cada tipo de lista de prueba (por ejemplo, lista ordenada, lista inversa, etc.)
    for tipo, lista in listas_prueba.items():
        # Crea una copia de la lista original para no modificarla durante el ordenamiento
        copia = lista.copy()
        # Ejecuta la función de ordenamiento sobre la copia y recibe la lista ordenada,
        # además de la cantidad de comparaciones e intercambios realizados
        ordenada, comparaciones, intercambios = funcion_ordenamiento(copia)
        # Imprime el tipo de lista que se está evaluando (por ejemplo, "Lista aleatoria")
        print(f"{tipo}:")
        # Imprime la cantidad de comparaciones realizadas por el algoritmo en esta lista
        print(f"  Comparaciones: {comparaciones}")
        # Imprime la cantidad de intercambios realizados por el algoritmo en esta lista
        print(f"  Intercambios: {intercambios}")
        # Imprime la lista ordenada resultante
        print(f"  Resultado: {ordenada}")

while True:
    print("---------------------------------------------------")  
    print("Bienvenido al programa de ordenamiento de precios")
    print("---------------------------------------------------")
    print("Seleccione el método de ordenamiento:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. Orden de listas ascendente, descendente o personalizada")
    print("5. Salir")
    
    opciones = int(input("Ingrese su opción: "))
    
    while opciones < 1 or opciones > 5:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        opciones = int(input("Ingrese su opción: "))
    
    if opciones == 1:
        while True:
            print("-------------------------------")
            print("Bubble Sort / Ordenamiento por burbuja")
            print("-------------------------------")
            print("1. Ordenar lista de precios")
            print("2. Ordenamientocon numeros por el usuario")
            print("3. Volver al menú principal")
            
            opcion_bubble = int(input("Seleccione una opción: "))
            while opcion_bubble < 1 or opcion_bubble > 3:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                opcion_bubble = int(input("Seleccione una opción: "))
                
            if opcion_bubble == 1:
                
                print("-------------------------------")
                print("Ordenar lista de precios")
                sorted_prices, comparisons, swaps = bubble_sort(precios_varios.copy())
                print("Lista ordenada con Bubble Sort:", sorted_prices)
                print("Comparaciones realizadas:", comparisons)
                print("Intercambios realizados:", swaps)
                
            elif opcion_bubble == 2:
                
                print("-------------------------------")
                print("Ordenamiento con numeros por el usuario")
                print("Ingreso de los precios")
                
                precios = []
                
                for i in range(10):
                    while True:
                        try:
                            precio = float(input(f"Ingrese el precio {i+1}: "))
                            precios.append(precio)
                            break
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número decimal o entero.")
                sorted_prices, comparisons, swaps = bubble_sort(precios)
                print("Lista ordenada con Bubble Sort:", sorted_prices)
                print("Comparaciones realizadas:", comparisons)
                print("Intercambios realizados:", swaps)
                
            elif opcion_bubble == 3:
                
                print("Volviendo al menú principal...")
                print("-------------------------------")
                break
            
    elif opciones == 2:
        while True:
            
            print("-------------------------------")
            print("Insertion Sort / Ordenamiento por inserción")
            print("-------------------------------")
            print("1. Ordenar lista de precios")
            print("2. Ordenamiento con numeros por el usuario")
            print("3. Volver al menú principal")
            
            opcion_insertion = int(input("Seleccione una opción: "))
            while opcion_insertion < 1 or opcion_insertion > 3:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                opcion_insertion = int(input("Seleccione una opción: "))
                
            if opcion_insertion == 1:
                
                print("-------------------------------")
                print("Ordenar lista de precios")
                sorted_prices, comparisons, swaps = insertion_sort(precios_varios.copy())
                print("Lista ordenada con Insertion Sort:", sorted_prices)
                print("Comparaciones realizadas:", comparisons)
                print("Intercambios realizados:", swaps)
                
            elif opcion_insertion == 2:
                
                print("-------------------------------")
                print("Ordenamiento con numeros por el usuario")
                print("Ingreso de los precios")
                
                precios = []
                
                for i in range(10):
                    while True:
                        try:
                            precio = float(input(f"Ingrese el precio {i+1}: "))
                            precios.append(precio)
                            break
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número decimal o entero.")
                sorted_prices, comparisons, swaps = insertion_sort(precios)
                print("Lista ordenada con Insertion Sort:", sorted_prices)
                print("Comparaciones realizadas:", comparisons)
                print("Intercambios realizados:", swaps)
                
            elif opcion_insertion == 3:
                print("Volviendo al menú principal...")
                print("-------------------------------")
                break
    elif opciones == 3:
        
        while True:
            
            print("-------------------------------")
            print("Selection Sort / Ordenamiento por selección")
            print("-------------------------------")
            print("1. Ordenar lista de precios")
            print("2. Ordenamiento con numeros por el usuario")
            print("3. Volver al menú principal")
            
            opcion_selection = int(input("Seleccione una opción: "))
            while opcion_selection < 1 or opcion_selection > 3:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                opcion_selection = int(input("Seleccione una opción: "))
                
            if opcion_selection == 1:
                
                print("-------------------------------")
                print("Ordenar lista de precios")
                sorted_prices, comparisons, swaps = selection_sort(precios_varios.copy())
                print("Lista ordenada con Selection Sort:", sorted_prices)
                print("Comparaciones realizadas:", comparisons)
                print("Intercambios realizados:", swaps)
                
            elif opcion_selection == 2:
                
                print("-------------------------------")
                print("Ordenamiento con numeros por el usuario")
                print("Ingreso de los precios")
                
                precios = []
                
                for i in range(10):
                    while True:
                        try:
                            precio = float(input(f"Ingrese el precio {i+1}: "))
                            precios.append(precio)
                            break
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número decimal o entero.")
                            
                sorted_prices, comparisons, swaps = selection_sort(precios)
                print("Lista ordenada con Selection Sort:", sorted_prices)
                print("Comparaciones realizadas:", comparisons)
                print("Intercambios realizados:", swaps)
                
            elif opcion_selection == 3:
                
                print("Volviendo al menú principal...")
                print("-------------------------------")
                break
    elif opciones == 4:
        print("---------------------------------------------------------")
        print("Orden de listas ascendente, descendente o personalizada")
        print("---------------------------------------------------------")
        
        mostrar_resultados("Bubble Sort", bubble_sort)
        mostrar_resultados("Insertion Sort", insertion_sort)
        mostrar_resultados("Selection Sort", selection_sort)
        
    elif opciones == 5:
        
        print("Saliendo del programa...")
        break



# * Explica cómo funciona cada algoritmo (brevemente, en tus propias palabras).
# Bubble Sort: Compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. 
# Repite el proceso varias veces hasta que toda la lista esté ordenada.

# Insertion Sort: Toma un elemento y lo coloca en su posición correcta dentro de una porción ya ordenada. 
# Es como ordenar cartas en la mano.

# Selection Sort: Busca el valor más pequeño en la parte no ordenada de la lista y lo coloca en su lugar correcto, 
# al principio. Repite este proceso hasta ordenar todo.

# * Compara sus rendimientos: ¿Cuál fue más eficiente en tu caso y por qué?
# Algoritmo	    Comparaciones	Intercambios
# Bubble Sort	        45	        17
# Insertion Sort	    18	        18
# Selection Sort	    45	        5
# Insertion Sort hizo menos comparaciones que Bubble y menos intercambios que Bubble (aunque más que Selection).

# * ¿En qué situaciones usarías cada uno en la vida real o en software?
# Algoritmo	                    Usar cuando
# Bubble Sort	            Para enseñanza o cuando el rendimiento no es una prioridad. Es muy fácil de entender.
# Insertion Sort	        Para listas pequeñas o casi ordenadas. Es rápido y eficiente en esos casos.
# Selection Sort	        Cuando queremos minimizar el número de intercambios, aunque tenga muchas comparaciones. 
#                           Ideal en dispositivos donde intercambiar datos es costoso.