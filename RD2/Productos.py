
# 1. ¿Qué es la búsqueda lineal? ¿Cómo funciona?

# La búsqueda line  al es un algoritmo que recorre una lista elemento por elemento hasta encontrar el valor 
# buscado o hasta terminar de revisar toda la lista.
# Cómo funciona:
# Empieza desde el primer elemento.
# Compara el valor buscado con cada elemento, uno por uno.
# Si lo encuentra, devuelve su posición.
# Si llega al final sin encontrarlo, indica que no está en la lista.
# Ejemplo:
#     def busqueda_lineal(lista, objetivo):
#     for i in range(len(lista)):
#         if lista[i] == objetivo:
#             return i
#     return -1

# 2. ¿Qué es la búsqueda binaria? ¿Qué condición especial debe cumplir la lista?

# La búsqueda binaria es un algoritmo eficiente que divide repetidamente 
# a la mitad una lista ordenada para encontrar un valor.
# La lista debe estar ordenada (de menor a mayor o viceversa).    
# Cómo funciona:
# Se compara el valor buscado con el elemento central.
# Si es igual, se devuelve la posición.
# Si es menor, se repite la búsqueda en la mitad izquierda.
# Si es mayor, en la mitad derecha.
# El proceso se repite hasta encontrar el valor o hasta que el rango se reduzca a cero.
# Ejemplo:
#     def busqueda_binaria(lista, objetivo):
#     inicio = 0
#     fin = len(lista) - 1

#     while inicio <= fin:
#         medio = (inicio + fin) // 2
#         if lista[medio] == objetivo:
#             return medio
#         elif lista[medio] < objetivo:
#             inicio = medio + 1
#         else:
#             fin = medio - 1
#     return -1

# 3. ¿En qué casos conviene usar cada una?

# Tipo de búsqueda	Cuándo usarla	            Ventajas	                                     Desventajas
# Lineal	       Lista pequeña o desordenada	Fácil de implementar, no necesita orden	          Lenta en listas grandes
# Binaria	       Lista grande y ordenada	     Muy rápida (O(log n))	                          Requiere orden previo


# Usa búsqueda lineal si la lista es pequeña o no está ordenada.
# Usa búsqueda binaria si la lista está ordenada y buscas eficiencia.

print("-------------------------------------------------------")
print("Productos Generales")
print("-------------------------------------------------------")

productos = [
    "laptop", "celular", "monitor", "teclado", "mouse", "cargador", "disco", "usb",
    "impresora", "hdmi", "bateria", "audifonos", "webcam", "bocinas", "silla",
    "escritorio", "hub", "pasta", "fuente", "tarjeta"
]
historial = []
while True:
    
    print("1. Busqueda de productos Lineal")
    print("2. Busqueda de productos Binaria")
    print("3. Historial de busquedas")
    print("4. Salir")
    try:
        opciones = int(input("Seleccione una opción: "))
        while opciones < 1 or opciones > 4:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            opciones = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        continue
    if opciones == 1:
        
        # Solicitar al usuario que ingrese el nombre del producto a buscar
        try:
            ingresar_nombre = input("Ingrese el nombre del producto que desea buscar: ")
        except ValueError:
            print("Error: La entrada no puede estar vacía.")
            continue
        
        #Busqueda lineas
        busqueda_lineal = 0
        encontrado = False
        
        for i, titulo in enumerate(productos):
            busqueda_lineal += 1
            if titulo.lower() == ingresar_nombre.lower():
                encontrado = True
                print(f"El producto '{titulo}' se encuentra en la lista.")
                print(f"Su posicion es: {i + 1}")
                break
        if not encontrado:
            print(f"El producto '{ingresar_nombre}' no se encuentra en la lista.")
        print(f"Comparaciones realizadas: {busqueda_lineal}")
        print("-------------------------------------------------------")
        
        historial.append({
            "tipo": "Lineal",
            "producto": ingresar_nombre,
            "resultado": "encontrado" if encontrado else "no encontrado",
            "comparaciones": busqueda_lineal
        })
        
    if opciones == 2:
        # Solicitar al usuario que ingrese el nombre del producto a buscar
        try:
            ingresar_nombre = input("Ingrese el nombre del producto que desea buscar: ")
        except ValueError:
            print("Error: Debe ingresar un nombre de producto válido.")
            continue
        
        #Busqueda binaria
        busqueda_binaria = 0
        encontrado = False
        
        # Ordenar la lista de productos
        productos.sort()
        
        inicio = 0
        fin = len(productos) - 1
        
        while inicio <= fin:
            medio = (inicio + fin) // 2
            busqueda_binaria += 1
            
            if productos[medio].lower() == ingresar_nombre.lower():
                encontrado = True
                print(f"El producto '{productos[medio]}' se encuentra en la lista.")
                print(f"Su posicion es: {medio + 1}")
                break
            elif productos[medio].lower() < ingresar_nombre.lower():
                inicio = medio + 1
            else:
                fin = medio - 1
        
        if not encontrado:
            print(f"El producto '{ingresar_nombre}' no se encuentra en la lista.")
        
        print(f"Comparaciones realizadas: {busqueda_binaria}")
        print("-------------------------------------------------------")
        
        historial.append({
            "tipo": "Binaria",
            "producto": ingresar_nombre,
            "resultado": "encontrado" if encontrado else "no encontrado",
            "comparaciones": busqueda_binaria
        })
    if opciones == 3:
        # Solicitar al usuario que ingrese el nombre del producto a buscar
        # Resumen final
        print("\n=== RESUMEN DE BÚSQUEDAS ===")
        if historial:
            for i, h in enumerate(historial, start=1):
                print(f"{i}. [{h['tipo']}] {h['producto']} - {h['resultado']} | Comparaciones: {h['comparaciones']}\n")
                print("-------------------------------------------------------")
        else:
            print("No se realizaron búsquedas.\n")
    if opciones == 4:
        print("Saliendo del programa...")
        break

# # Resumen final
# print("\n=== RESUMEN DE BÚSQUEDAS ===")
# if historial:
#     for i, h in enumerate(historial, start=1):
#         print(f"{i}. [{h['tipo']}] {h['producto']} - {h['resultado']} | Comparaciones: {h['comparaciones']}")
# else:
#     print("No se realizaron búsquedas.")