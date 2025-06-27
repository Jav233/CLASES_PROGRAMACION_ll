# Definimos una clase simple de cola con prioridad (usamos lista para hacerlo didáctico)

class prioridadHospital:
    # Método constructor, se llama al crear el objeto
    def __init__(self):
        # Creamos una lista vacía
        self.items = []
        
    # Método para agregar elementos a la cola
    def enconlar (self, paciente, prioridad):
        # Agregamos el nuevo elemento como una tupla 
        self.items.append((paciente, prioridad))
        # Mostramos mensaje indicando qué elemento fue ingresado

        print(f"Ingresó: {paciente} con prioridad {prioridad}")
    # Método que verifica si la cola está vacía
    def estavacia(self):
        if not self.items:
            print("La cola está vacía.")
            return True
        else:
            print("La cola no está vacía.")
            return False
        # Método para eliminar el elemento con mayor prioridad 
    def desencolar(self):
        # Primero verificamos que la cola no esté vacía
        if not self.estavacia():
            # Ordenar por prioridad (menor es mejor)
            self.items.sort(key=lambda x: x[1])
            # Extraemos el primer elemento (mayor prioridad)
            paciente, prioridad = self.items.pop(0)
            
            # Retornamos el elemento atendido por si se necesita usarprint(f"Atendiendo a: {paciente} con prioridad {prioridad}")
            return paciente
        else:
            # Si la cola está vacía, informamos
            print("No hay pacientes para atender.")
            return None
        # Método que retorna el tamaño actual de la cola
    def tamaño(self):
        return len(self.items)
    # Método para mostrar los pacientes en la cola
    
    def mostrar(self):
        if self.estavacia():
            print("-------------------------------")
            print("No hay pacientes en la cola.")
            print("-------------------------------")
        else:
            print(f"{'Paciente':<15}{'Prioridad':<10}")
            print("-" * 25)
            for paciente, prioridad in sorted(self.items, key=lambda x: x[1]):
                print(f"{paciente:<15}{prioridad:<10}")

    
# Creamos la cola con prioridad  
cola_hospital = prioridadHospital()

# Encolamos algunos clientes


# while not cola_hospital.estavacia():
#     # Mostramos los pacientes en la cola
#     cola_hospital.mostrar()
#     # Desencolamos al paciente con mayor prioridad
#     atendido = cola_hospital.desencolar()
#     if atendido:
#         print(f"Atendiendo a: {atendido}")
#     print()  # Línea en blanco para mejor legibilidad entre iteraciones

while True:
    try:
        # Mostramos los pacientes en la cola
        print("------------------------------------------------------------")
        print("/////Bienvenido al sistema de atención hospitalaria/////")
        print("------------------------------------------------------------")
        print("1. Agregar pacientes indicando su nombre y prioridad")
        print("2. Atender paciente con mayor prioridad")
        print("3. Mostrar cuantos pacientes hay en la cola")
        print("4. Mostrar la lista de pacientes pendientes de atención")
        print("5. Salir")
        print("------------------------------------------------------------")

        opcion = int(input("Seleccione una opción: "))
        while opcion < 1 or opcion > 5:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")
            opcion = int(input("Seleccione una opción: "))
            
        if opcion == 1:
            print("Ingrese los datos del paciente:")
            for i in range(8):
                print(f"Paciente {i + 1}:")
                nombre = input("Ingrese el nombre del paciente: ").capitalize()
                prioridad = int(input("Ingrese la prioridad del paciente (1-4, siendo 1 la más alta): "))
                while prioridad < 1 or prioridad > 4:
                    print("Prioridad no válida. Debe ser un número entre 1 y 4.")
                    prioridad = int(input("Ingrese la prioridad del paciente (1-4, siendo 1 la más alta): "))
                cola_hospital.enconlar(nombre, prioridad)
        elif opcion == 2:
            
            atendido = cola_hospital.desencolar()
            if atendido:
                print(f"Atendiendo a: {atendido}")
            print()
        elif opcion == 3:
            print("Mostrando la cantidad de pacientes en la cola...")
            print("------------------------------------------------------------")
            print(f"Cantidad de pacientes en la cola: {cola_hospital.tamaño()}")
            print("------------------------------------------------------------")
        elif opcion == 4:
            print("Mostrando la lista de pacientes pendientes de atención...")
            print("------------------------------------------------------------")
            cola_hospital.mostrar()
            print("------------------------------------------------------------")
        elif opcion == 5:
            print("Saliendo del sistema. ¡Gracias por usarlo!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    