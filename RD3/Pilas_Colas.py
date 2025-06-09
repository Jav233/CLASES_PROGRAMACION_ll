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

#is_empty verifica si la pila está vacía
if not pila:
    print("La pila está vacía")
else:
    print("La pila no está vacía, contiene elementos")

pilas = []

#Push
pilas.append("Tarea 1")
pilas.append("Tarea 2")
#peek
print(f"Última tarea en la pila: {pilas[-1]}")
#Pop
tarea_eliminada = pilas.pop()
print(f"Tarea eliminada: {tarea_eliminada}")
#Ver lista de tareas en la pila
print(f"Pila de tareas actual: {pilas}")
#is_empty
if not pilas:
    print("La pila está vacía")
else:
    print("La pila no está vacía, contiene tareas")
    