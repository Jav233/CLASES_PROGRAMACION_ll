#Funcion para buscar un elemento en una lista de frutas de forma binaria
def busqueda_binaria(lista, objetivo):
    particiones = 0 # Contador de particiones
    inicio = 0 # Indice inicial
    fin = len(lista) - 1 # Indice final
    while inicio <= fin: # Mientras el indice inicial sea menor o igual al indice final
        particiones += 1    # Incrementa el contador de particiones
        medio = (inicio + fin) // 2 # Calcula el indice medio
        if lista[medio] == objetivo: # Si el elemento en el indice medio es igual al objetivo
            print(f"Particiones realizadas: {particiones}") # Imprime el contador de particiones
            return medio #Devuleve el indice donde se encontro
        elif lista[medio] < objetivo: # Si el elemento en el indice medio es menor que el objetivo
            inicio = medio + 1 # Actualiza el indice inicial
        else:
            fin = medio - 1 # Actualiza el indice final
    print(f"Particiones realizadas: {particiones}") # Imprime el contador de particiones
    return -1 #No encontrado

#Lista de numeros ordenados
numeros_intervalos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
buscar_numero = int(input("Ingrese el numero que desea buscar: ")) # Pregunta al usuario que numero desea buscar

buscar = busqueda_binaria(numeros_intervalos, buscar_numero) # Llama a la funcion de busqueda binaria y guarda el resultado en la variable buscar

if buscar != -1: # Si el numero se encuentra en la lista
    print(f"El numero {buscar_numero} se encuentra en la lista.")   # Imprime que el numero se encuentra en la lista
    print(f"Su posicion es: {buscar+1}") # Imprime la posicion del numero en la lista
    
else:
    print("El numero no se encuentra en la lista.") # Imprime que el numero no se encuentra en la lista
    

