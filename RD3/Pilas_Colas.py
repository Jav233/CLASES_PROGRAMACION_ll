pila = []

# Push agrega un elemento al final de la pila
pila.append("Plato 1")
pila.append("Plato 2")
pila.append("Plato 3")

#Ver lista de platos en la pila
print(f"Pila actual: {pila}")

#Pop elimina el último elemento de la pila
plato_eliminado = pila.pop()
print(f"Plato eliminado: {plato_eliminado}")
print(f"Pila actual después de eliminar: {pila}")

#Peek muestra el último elemento de la pila sin eliminarlo
if pila:
    print(f"Último plato en la pila: {pila[-1]}")
else:
    print("La pila está vacía")
    