#Funcion para buscar un elemento en una lista de frutas de forma binaria
def busqueda_lineal(lista, elemento): # Esta funcion busca un elemento en una lista de forma lineal
    comparaciones = 0 # Contador de comparaciones
    for i in range(len(lista)): # Recorre la lista
        comparaciones += 1 # Incrementa el contador de comparaciones
        if lista[i] == elemento: # Si el elemento es igual al que se busca
            print(f"Comparaciones realizadas: {comparaciones}") # Imprime el contador de comparaciones
            return i # Devuelve el indice donde se encontro
    print(f"Comparaciones realizadas: {comparaciones}") # Imprime el contador de comparaciones
    return -1 # Si no se encuentra el elemento devuelve -1

# Lista de frutas
frutas = ['manzana', 'banana', 'cereza', 'pera', 'kiwi','mora','sandia','melon','naranja','limon']
#Titulo del programa
print("-------------------------------")
print("Lista de frutas")
print("-------------------------------")

# Pregunta al usuario que fruta desea buscar
furta = input("Ingrese el nombre de la fruta que desea buscar: ")
encontrar = busqueda_lineal(frutas, furta) # Llama a la funcion de busqueda lineal y guarda el resultado en la variable encontrar

if encontrar != -1: # Si la fruta se encuentra en la lista
    print(f"La fruta {furta.capitalize()} se encuentra en la lista.") # Imprime que la fruta se encuentra en la lista
    print(f"Su posicion es: {encontrar+1}") # Imprime la posicion de la fruta en la lista

else: # Si la fruta no se encuentra en la lista
    print(f"La fruta {furta} no se encuentra en la lista.") # Imprime que la fruta no se encuentra en la lista
    
print("-------------------------------")

