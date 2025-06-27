# Importamos la clase deque desde el módulo collections, que permite crear colas de manera eficiente.
from collections import deque

# Importamos el módulo time para simular pausas entre turnos (espera del viaje).
import time

# Importamos random para generar nombres aleatorios de personas y decidir si tienen prioridad.
import random

# Creamos una cola vacía para personas que hacen fila normalmente.
cola_general = deque()

# Creamos una cola separada para personas con prioridad (niños, discapacidad, fast pass).
cola_prioritaria = deque()
# Creamos una cola para personas con discapacidad, si se desea manejar por separado.
cola_discapacidad = deque()


CAPACIDAD_VAGON = 4 # Definimos la capacidad máxima del vagón de la montaña rusa: solo pueden subir 4 personas por viaje.
DURACION_VIAJE = 3 # Definimos la duración del viaje en turnos. Cada viaje tarda 3 "unidades de tiempo".

def generar_ticket(nombre, tipo, viaje):
    print("========== TICKET ==========")
    print(f"Nombre del visitante: {nombre}")
    print(f"Tipo de acceso: {tipo}")
    print(f"Número de viaje: {viaje}")
    print("¡Gracias por visitar K-Boom Park!")
    print("============================\n")

# Esta función agrega personas a la cola correspondiente.
# Recibe un nombre (string) y una bandera de prioridad (True o False).
def agregar_persona(discap, prior, general):
    while True:
        try:
            nombre = input("Ingrese el nombre de la persona: ").capitalize()
            if not nombre.isalpha():
                print("El nombre debe contener solo letras.")
                continue

            print("Seleccione el tipo de acceso:")
            print("1. Discapacidad")
            print("2. Prioridad")
            print("3. General")
            tipo = input("Opción (1/2/3): ")

            while tipo not in ['1', '2', '3']:
                print("Opción inválida. Elija 1, 2 o 3.")
                tipo = input("Opción (1/2/3): ")

            if tipo == '1':
                discap.append(nombre)
                print(f"{nombre} agregado a la cola de discapacidad.")
                generar_ticket(nombre, "Discapacidad", 0)  # ← ticket solo aquí
            elif tipo == '2':
                prior.append(nombre)
                print(f"{nombre} agregado a la cola prioritaria.")
                generar_ticket(nombre, "Prioridad", 0)
            elif tipo == '3':
                general.append(nombre)
                print(f"{nombre} agregado a la cola general.")
                generar_ticket(nombre, "General", 0)
            break
        except Exception as e:
            print(f"Error: {e}. Intente de nuevo.")


# Esta función muestra el estado actual de ambas colas.
# Convierte las colas a listas para que se muestren bien por consola.
def mostrar_colas():
    print("\nEstado actual de las colas:\n")
    print("Cola de Discapacidad:", list(cola_discapacidad))
    print("Cola Prioritaria:", list(cola_prioritaria))
    print("Cola General:", list(cola_general))

# Esta función simula el viaje de la montaña rusa.
# Recibe la lista de pasajeros y el número del viaje actual.
def simular_viaje(pasajeros, numero_viaje):
    print(f"\n🎢 Viaje #{numero_viaje} iniciado")
    print("Pasajeros a bordo:")
    
    for nombre, tipo in pasajeros:
        generar_ticket(nombre, tipo, numero_viaje)
    # Imprimimos el inicio del viaje con los nombres de los pasajeros que subieron.
    #print(f"\n Viaje #{numero_viaje} con: {pasajeros}")
    # for i, (nombre, tipo) in enumerate(pasajeros, start=1):
    #     print(f"  {i}. {nombre} | Tipo de acceso: {tipo} | Viaje: {numero_viaje}")
    # Simulamos el viaje mediante un ciclo que dura la cantidad de turnos definida.
    for t in range(DURACION_VIAJE):
        # Imprime el turno actual dentro del viaje (por ejemplo: Turno 1/3)
        print(f"  Turno {t+1}/{DURACION_VIAJE}")
        # Pausa el programa 1 segundo para simular que el viaje está en progreso.
        time.sleep(1)
        
    print("\n🎟️ Tickets de este viaje:")
    
    
    # Al finalizar todos los turnos, mostramos un mensaje celebrando el fin del viaje.
    print("¡Viaje finalizado!")

def iniciar_simulacion(turnos_totales, numero_viaje, contadores, colas):
    discap, prior, general = colas
    total_atendidos, total_discapacidad, total_prioridad, total_general = contadores

    for turno in range(1, turnos_totales + 1):
        print(f"\n--- Turno {turno}/{turnos_totales} ---")

        # Si hay suficientes personas para un viaje
        total_en_colas = len(discap) + len(prior) + len(general)
        if total_en_colas >= CAPACIDAD_VAGON:
            numero_viaje += 1
            pasajeros = []

            while len(pasajeros) < CAPACIDAD_VAGON:
                if len(discap) > 0:
                    nombre = discap.popleft()
                    pasajeros.append((nombre, "Discapacidad"))
                    total_discapacidad += 1
                elif len(prior) > 0:
                    nombre = prior.popleft()
                    pasajeros.append((nombre, "Prioridad"))
                    total_prioridad += 1
                elif len(general) > 0:
                    nombre = general.popleft()
                    pasajeros.append((nombre, "General"))
                    total_general += 1
                else:
                    break  # por si acaso

            total_atendidos += len(pasajeros)
            simular_viaje(pasajeros, numero_viaje)
        else:
            print("No hay suficientes personas en las colas para el viaje.")

    contadores = (total_atendidos, total_discapacidad, total_prioridad, total_general)
    return numero_viaje, contadores


# Esta función controla la simulación completa durante varios turnos.
# Recibe como parámetro la cantidad total de turnos a ejecutar.


# Calcular promedio
def mostrar_resumen(contadores, numero_viaje):
    total_atendidos, total_discapacidad, total_prioridad, total_general = contadores

    if numero_viaje > 0:
        promedio_por_viaje = total_atendidos / numero_viaje
    else:
        promedio_por_viaje = 0

    print("\n====== RESUMEN DE LA SIMULACIÓN ======")
    print(f"Total de personas atendidas: {total_atendidos}")
    print(f" - Personas con discapacidad: {total_discapacidad}")
    print(f" - Personas con prioridad: {total_prioridad}")
    print(f" - Personas en acceso general: {total_general}")
    print(f"Total de viajes realizados: {numero_viaje}")
    print(f"Promedio de personas por viaje: {promedio_por_viaje:.2f}")
    print("======================================")


# Llamar a la función principal
#iniciar_simulacion(turnos_totales=10)

def main():
    numero_viaje = 0
    contadores = (0, 0, 0, 0)  # total_atendidos, discapacidad, prioridad, general
    colas = (cola_discapacidad, cola_prioritaria, cola_general)
    
    while True:
        try:
            
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Agregar persona")
            print("2. Ver estado de las colas")
            print("3. Simular viaje")
            print("4. Mostrar resumen")
            print("5. Salir del sistema")

            opcion = input("Seleccione una opción (1-5): ")
            while opcion not in ['1', '2', '3', '4', '5']:
                print("Opción inválida. Por favor, elija una opción válida.")
                opcion = input("Seleccione una opción (1-5): ")

            if opcion == '1':
                agregar_persona(cola_discapacidad, cola_prioritaria, cola_general)
                
            elif opcion == '2':
                print("→ Ver estado de las colas ")
                mostrar_colas()
                #ticket()  # Mostrar resumen de la simulación
            elif opcion == '3':
                try:
                    numero_viaje, contadores = iniciar_simulacion(1, numero_viaje, contadores, colas)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            elif opcion == '4':
                
                mostrar_resumen(contadores, numero_viaje)
            elif opcion == '5':
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")

# Ejecutar menú
main()

# Esta función simula el proceso de llenar el vagón antes del viaje.
# def cargar_vagon(viaje_n, contadores, colas):
#     pasajeros = []
#     discap, prior, general = colas
#     total_atendidos, total_discapacidad, total_prioridad, total_general = contadores
#     viaje_n += 1

#     while len(pasajeros) < CAPACIDAD_VAGON:
#         if discap:
#             nombre = discap.popleft()
#             pasajeros.append(nombre)
#             total_discapacidad += 1
#             total_atendidos += 1
#             generar_ticket(nombre, "Discapacidad", viaje_n)
#         elif prior:
#             nombre = prior.popleft()
#             pasajeros.append(nombre)
#             total_prioridad += 1
#             total_atendidos += 1
#             generar_ticket(nombre, "Prioridad", viaje_n)
#         elif general:
#             nombre = general.popleft()
#             pasajeros.append(nombre)
#             total_general += 1
#             total_atendidos += 1
#             generar_ticket(nombre, "General", viaje_n)
#         else:
#             break

#     contadores = (total_atendidos, total_discapacidad, total_prioridad, total_general)
#     return viaje_n, contadores, pasajeros  # ← ahora devuelve 3 valores