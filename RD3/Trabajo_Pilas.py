class PilaTareas:
    def __init__(self):
        self.items = []
        
    def agregar_tarea(self, tarea):
        
        self.items.append(tarea)
        
        
    def terminar_tarea(self):
        if len(self.items) > 0:
            tarea_terminada = self.items.pop()
            print(f"Tarea terminada: {tarea_terminada}")
            return tarea_terminada

    def ver_ultima_tarea(self):
        
        if len(self.items) > 0:
            ultima_pos = len(self.items)
            ultima_tarea = self.items[-1]
            print(f"{ultima_pos}. {ultima_tarea}")
            return ultima_tarea
        else:
            print("No hay tareas en la pila.")
            return None
        
    def tamaño(self):
        
        return len(self.items)
    
    def mostrar_tareas(self):
        """Muestra todas las tareas en la pila."""
        if len(self.items) > 0:
            print("Tareas registradas:")
            for i, tarea in enumerate(self.items, start=1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas en la pila.")

        
#Crea la instancia y simula 10 tareas
pila = PilaTareas()
#pila.agregar_tarea("... tarea ...")

# - agregar_tarea(tarea)
# - terminar_tarea()
# - ver_ultima_tarea()
# - tamaño()

while True:
    try:
        print("\n Bienvenido al sistema de gestión de tareas")
        print("1. Agregar tarea")
        print("2. Terminar tarea")
        print("3. Ver última tarea")
        print("4. Ver tamaño de la pila")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        while opcion < 1 or opcion > 5:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            cont = 0
            for i in range(10):
                # Simula agregar 10 tareas
                cont += 1
                tarea = input(f"Ingrese la tarea {cont} a agregar: ").capitalize()
            #pila.agregar_tarea(tarea)
                pila.agregar_tarea(tarea)
                
        elif opcion == 2:
            pila.terminar_tarea()
        elif opcion == 3:
            ultima_tarea = pila.ver_ultima_tarea()
            if ultima_tarea:
                print(f"La última tarea es: {ultima_tarea}")
        elif opcion == 4:
            print(f"Tamaño de la pila: {pila.tamaño()}")
            pila.mostrar_tareas()
        elif opcion == 5:
            print("Saliendo del sistema de gestión de tareas.")
            break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    