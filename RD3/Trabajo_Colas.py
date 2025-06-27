class ColaPrioridadClientes:
    def __init__(self):
        self.items = []
        
    def agregar_cliente(self, nombre, prioridad):
        self.items.append(( prioridad,  nombre))
        print(f"Ingresó: {nombre} con prioridad {prioridad}")
        
    def atender_cliente(self):
        
        # Primero verificamos que la cola no esté vacía
        if not self.estavacia():
            # Ordenar por prioridad (menor es mejor)
            self.items.sort(key=lambda x: x[0])
            # Extraemos el primer elemento (mayor prioridad)
            prioridad, nombre = self.items.pop(0)
            
            # Retornamos el elemento atendido por si se necesita usarprint(f"Atendiendo a: {cliente} con prioridad {prioridad}")
            return nombre
        else:
            # Si la cola está vacía, informamos
            print("No hay pacientes para atender.")
            return None
        
    def mostrar_pendientes(self):
        if not self.estavacia():
            print(f"{'Cliente':<15}{'Prioridad':<10}")
            print("-" * 25)
            for prioridad, nombre in sorted(self.items, key=lambda x: x[0]):
                print(f"{nombre:<15}{prioridad:<10}")
                
        
    def tamaño(self):
        """Retorna el número de clientes en la cola."""
        return len(self.items)
    
    def estavacia(self):
        if not self.items:
            print("La cola está vacía.")
            return True
        else:
            print("La cola no está vacía.")
            return False

# Crea la instancia de la cola de prioridad
cola_clientes = ColaPrioridadClientes()

while True:
    try:
        print("\nBienvenido al sistema de gestión de clientes")
        print("1. Agregar cliente")
        print("2. Atender cliente")
        print("3. Ver clientes pendientes")
        print("4. Ver tamaño de la cola")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        while opcion < 1 or opcion > 5:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            for i in range(8):
                #print(f"Ingrese los datos del cliente {i + 1}:")
                nombre = input(f"Ingrese el nombre del cliente {i+1}: ").capitalize()
                while True:
                    try:
                        prioridad = int(input("Ingrese la prioridad del cliente (1-4, donde 1 es la más alta): "))
                        while prioridad < 1 or prioridad > 4:
                            print("Prioridad inválida. Debe ser un número entre 1 y 4.")
                            prioridad = int(input("Ingrese la prioridad del cliente (1-4, donde 1 es la más alta): "))
                        break
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número entero.")
                cola_clientes.agregar_cliente(nombre, prioridad)
                print(f"Cliente {nombre} agregado con prioridad {prioridad}.")
        elif opcion == 2:
            atendido = cola_clientes.atender_cliente()
            if atendido:
                print(f"Cliente atendido: {atendido}")
            print()
        elif opcion == 3:
            print("Clientes pendientes:")
            cola_clientes.mostrar_pendientes()
        elif opcion == 4:
            print(f"Tamaño de la cola: {cola_clientes.tamaño()}")
            #cola_clientes.mostrar_pendientes()
        elif opcion == 5:
            print("Saliendo del sistema de gestión de clientes.")
            break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")