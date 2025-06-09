# Creamos una pila vacía para almacenar tareas pendientes
tareas_original = []
# Agregamos tres tareas a la pila
tareas_original.append("Estudiar pilas en Python")
tareas_original.append("Hacer ejercicios de estructuras de datos")
tareas_original.append("Leer documentación oficial de Python")

tarea_modificada = tareas_original.copy()
# Mostramos el estado actual de la pila
print("Tareas pendientes:", tareas_original)

# Mostramos la tarea más reciente (el tope de la pila)
if tarea_modificada:
    print("Tarea más reciente:", tarea_modificada[-1])
else:
    print("No hay tareas pendientes.")
    
# Quitamos la última tarea (la más reciente)

if tarea_modificada:
    completada = tarea_modificada.pop()
    print("Tarea completada:", completada)
else:
    print("No hay tareas para completar.")

# Verificamos si aún hay tareas pendientes
if len(tarea_modificada) == 0:
    print("Todas las tareas han sido completadas.")
else:
    print("Tareas restantes:", tarea_modificada)

print("Estado inicial de la pila:", tareas_original)
#print("Tareas pendientes:", tarea_modificada)

