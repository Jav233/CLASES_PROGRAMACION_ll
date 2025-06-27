from collections import deque

#Creamos una cola vacia
cola = deque()

# Añadimos elementos a la cola
cola.append("A")
cola.append("B")
cola.append("C")

# Imprimimos la cola
print(cola)

# Eliminamos un elemento de la cola
primero = cola.popleft()
print("Elemento atendido:", primero)
print("Cola actual:", cola)

#deque es mas eficiente que las listas para operaciones de inserción y eliminación en ambos extremos
