class NodoDobleque:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

#crear nodos 
nodo1 = NodoDobleque('A')
nodo2 = NodoDobleque('B')
nodo3 = NodoDobleque('C')

# Enlazar nodos
nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2

# Imprimir la lista enlazada doble
print(nodo1.dato)  # imprime A
print(nodo2.dato)  # imprime B
print(nodo3.dato)  # imprime C

# Imprimir en orden inverso
print(nodo3.dato)  # imprime C
print(nodo2.dato)  # imprime B
print(nodo1.dato)  # imprime A
