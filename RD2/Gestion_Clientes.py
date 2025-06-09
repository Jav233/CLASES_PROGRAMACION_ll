
clientes = [
    ("Javier", 100.0),
    ("Pedro", 50.50),
    ("Estevan", 20.90),
    ("Jorge", 85.0),
    ("Dilon", 20.99),
    ("Alejo", 65.85),
    ("Rich", 64.23),
    ("Gabriel", 215.54),
    ("Edison", 19.21),
    ("Leonardo", 35.40)
]

def insertion_sort_por_nombre(clientes):
    for i in range(1, len(clientes)):
        key = clientes[i]
        j = i - 1
        while j >= 0 and key[0] < clientes[j][0]:
            clientes[j + 1] = clientes[j]
            j -= 1
        clientes[j + 1] = key
    return clientes

def selection_sort_por_saldo(clientes):
    n = len(clientes)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if clientes[j][1] < clientes[min_index][1]:
                min_index = j
        clientes[i], clientes[min_index] = clientes[min_index], clientes[i]
    return clientes

def busqueda_binaria(ordenada, objetivo):
    
    inicio = 0
    fin = len(ordenada) - 1
    comparaciones = 0

    while inicio <= fin:
        comparaciones += 1
        medio = (inicio + fin) // 2
        nombre = ordenada[medio][0].lower()

        if nombre == objetivo.lower():
            return medio, comparaciones
        elif objetivo.lower() < nombre:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1, comparaciones

def busqueda_lineal(clientes, objetivo):
    comparaciones = 0
    for i, cliente in enumerate(clientes):
        comparaciones += 1
        if cliente[0].lower() == objetivo.lower():
            return i, comparaciones
    return -1, comparaciones


while True:
    
    print("-------------------------------------------")
    print("Gestion de Clientes")
    print("-------------------------------------------")
    
    print("--------------------------")
    print("1. Lista de clientes")
    print("2. Tipos de ordenamiento")
    print("3. Buscar cliente")
    print("4. Agregar cliente")
    print("5. Salir")
    print("--------------------------")
    
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número.")
        continue
    while opcion < 1 or opcion > 5:
        print("Opcion invalida. Intente de nuevo.")
        opcion = int(input("Seleccione una opcion: "))
        
    if opcion == 1:
        print("Lista de clientes:")
        
        print("|| {:<10} || {:>10} ||".format("Cliente", "Saldo"))
        print("-" * 31)
        for cliente in clientes:
            print("|| {:<10} || ${:>8.2f}  ||".format(cliente[0], cliente[1]))
    
    elif opcion == 2:
        while True:
            print("---------------------------")
            print("Tipos de Ordenamiento:")
            print("1. Ordenar por nombre")
            print("2. Ordenar por saldo")
            print("3. Volver al menú principal")
            print("---------------------------")
            try:
                tipo_ordenamiento = int(input("Seleccione un tipo de ordenamiento: "))
                while tipo_ordenamiento < 1 or tipo_ordenamiento > 3:
                    print("Opcion invalida. Intente de nuevo.")
                    tipo_ordenamiento = int(input("Seleccione un tipo de ordenamiento: "))
                
                if tipo_ordenamiento == 1:
                    
                    print("Ordenando por nombre")
                    clientes_ordenados = insertion_sort_por_nombre(clientes.copy())
                    print("Clientes ordenados por nombre:")
                    print("|| {:<10} || {:>10} ||".format("Cliente", "Saldo"))
                    print("-" * 31)
                    for cliente in clientes_ordenados:
                        print("|| {:<10} || ${:>8.2f}  ||".format(cliente[0], cliente[1]))
                
                        
                elif tipo_ordenamiento == 2:
                    
                    print("Ordenando por saldo")
                    clientes_ordenados = selection_sort_por_saldo(clientes.copy())
                    print("Clientes ordenados por saldo:")
                    print("|| {:<10} || {:>10} ||".format("Cliente", "Saldo"))
                    print("-" * 31)
                    for cliente in clientes_ordenados:
                        print("|| {:<10} || ${:>8.2f}  ||".format(cliente[0], cliente[1]))
                
                elif tipo_ordenamiento == 3:
                    print("Volviendo al menú principal...")
                    break
            
            except ValueError:
                    print("Entrada inválida. Intente nuevamente.") 
                
    elif opcion == 3:
        while True:
            print("---------------------------")
            print("Buscar Cliente:")
            print("1. Búsqueda lineal")
            print("2. Búsqueda binaria")
            print("3. Volver al menú principal")
            print("---------------------------")
            try:
                metodo_busqueda = int(input("Seleccione el método de búsqueda: "))
                
                while metodo_busqueda < 1 or metodo_busqueda > 3:
                    print("Opcion invalida. Intente de nuevo.")
                    metodo_busqueda = int(input("Seleccione el método de búsqueda: "))
                if metodo_busqueda == 1:
                    print("Búsqueda lineal:")
                    nombre = input("Ingrese el nombre del cliente a buscar: ").lower()
                    indice, comparaciones = busqueda_lineal(clientes, nombre)
                    if indice != -1:
                        cliente = clientes[indice]
                        print(f"Cliente encontrado: {cliente[0]} ")
                        print(f"Saldo del cliente: ${cliente[1]:.2f}")
                        print(f"Comparaciones realizadas: {comparaciones}")
                    else:
                        print(f"Cliente '{nombre}' no encontrado. Comparaciones realizadas: {comparaciones}")
                        
                elif metodo_busqueda == 2:
                    print("Búsqueda binaria:")
                    if not clientes:
                        print("No hay clientes para buscar.")
                        continue
                    nombre = input("Ingrese el nombre del cliente a buscar: ").lower()
                    clientes_ordenados = insertion_sort_por_nombre(clientes.copy())
                    indice, comparaciones = busqueda_binaria(clientes_ordenados, nombre)
                    if indice != -1:
                        cliente = clientes_ordenados[indice]
                        print(f"Cliente encontrado: {cliente[0]}")
                        print(f"Saldo del cliente: ${cliente[1]:.2f}")
                        print(f"Comparaciones realizadas: {comparaciones}")
                    else:
                        print(f"Cliente '{nombre}' no encontrado. Comparaciones realizadas: {comparaciones}")
                    
                elif metodo_busqueda == 3:
                    break
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")
    elif opcion == 4:
        
        print("Agregar Cliente")
        try:
            nombre = str(input("Ingrese el nombre del nuevo cliente: ")).capitalize()
            saldo = float(input("Ingrese el saldo del nuevo cliente: "))
            clientes.append((nombre.capitalize(), saldo))
            print(f"Cliente '{nombre}' agregado con saldo ${saldo:.2f}.")
            #break
        except ValueError:
            print("Saldo inválido. Debe ingresar un número.")
            
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break
            
            
        
        
        
    
    
    
    
