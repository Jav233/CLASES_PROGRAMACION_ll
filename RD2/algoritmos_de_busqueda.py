#Es un metodo para encontrar un elemento dentro de una estructura de datos

lista = [1,2,3,4,5,6,7,8,9,10,10]
lista_nueva = [] 
for i in  lista:
    if i != 10:
        lista_nueva.append(i)
print(lista_nueva)

#########################################################################################
#Encontrar la posicion o existencia de un elemento dentro de una estructura de datos.
#Busqueda lineal
#Recorre uno a uno de una lista o arreglo desde el principio hasta el final

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i #Devuleve el indice donde se encontro
    return -1 #No encontrado
busqueda_lineal([1,2,3,4,5,6,7,8,9], 5) #Devuleve 4
busqueda_lineal([1,2,3,4,5,6,7,8,9], 10) #Devuleve -1

def busqueda_lineal_2(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1 #No encontrado

datos = [12,5,8,21,9]
print(busqueda_lineal_2(datos, 21)) #Devuleve 3

#Busqueda binaria

lista = [2,5,8,4,10,0,1,3,6,7,9]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
print(lista) #Devuleve [2, 4, 5, 8, 10]


for i in range(1, len(lista)):
    valor_actual = lista[i]
    pos = i
    
    while pos > 0 and lista[pos - 1] > valor_actual:
        lista[pos] = lista[pos - 1]
        pos -= 1
    
    lista[pos] = valor_actual
print(lista) #Devuleve [2, 4, 5, 8, 10]

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio #Devuleve el indice donde se encontro
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1 #No encontrado

datos_ordenados = [1,2,3,4,5,6,7,8,9,10]
print(busqueda_binaria(datos_ordenados, 5)) #Devuleve 4
#busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 5) #Devuleve 4

#Trabajo en clase 

            
            
            

    