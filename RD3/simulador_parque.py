
from collections import deque
import time

# Estructuras de colas
cola_general = deque()
cola_prioritaria = deque()
cola_discapacidad = deque()

# Constantes de simulación
CAPACIDAD_VAGON = 4
DURACION_VIAJE = 3

# Estadísticas
viajes_realizados = 0
total_atendidos = 0
atendidos_general = 0
atendidos_prioridad = 0
atendidos_discapacidad = 0

# Tiempo de espera por turno (por defecto 1 segundo)
espera_turno = 1


def agregar_visitante_manual():
    nombre = input("Nombre del visitante: ").strip()
    print("Tipo de acceso:\n1. General\n2. Prioridad\n3. Discapacidad")
    tipo = input("Selecciona el tipo (1/2/3): ")

    if tipo == "1":
        cola_general.append(nombre)
        print(f"{nombre} agregado a la cola General.")
    elif tipo == "2":
        cola_prioritaria.append(nombre)
        print(f"{nombre} agregado a la cola Prioritaria.")
    elif tipo == "3":
        cola_discapacidad.append(nombre)
        print(f"{nombre} agregado a la cola Discapacidad.")
    else:
        print("Opción inválida. No se agregó el visitante.")


def mostrar_colas():
    print("\n--- ESTADO ACTUAL DE LAS COLAS ---")
    print("Cola Discapacidad:", list(cola_discapacidad))
    print("Cola Prioritaria:", list(cola_prioritaria))
    print("Cola General:", list(cola_general))


def cargar_vagon():
    pasajeros = []

    while len(pasajeros) < CAPACIDAD_VAGON:
        if cola_discapacidad:
            pasajeros.append(("Discapacidad", cola_discapacidad.popleft()))
        elif cola_prioritaria:
            pasajeros.append(("Prioridad", cola_prioritaria.popleft()))
        elif cola_general:
            pasajeros.append(("General", cola_general.popleft()))
        else:
            break

    return pasajeros


def generar_ticket(nombre, tipo, viaje):
    print("\n🎟️ TICKET DE INGRESO 🎟️")
    print(f"Nombre: {nombre}")
    print(f"Acceso: {tipo}")
    print(f"Viaje N.º: {viaje}")
    print("¡Gracias por visitar K-Boom Park!")
    print("-----------------------------")


def simular_viaje(pasajeros, numero_viaje):
    global total_atendidos, atendidos_general, atendidos_prioridad, atendidos_discapacidad

    print(f"\n🎢 Iniciando Viaje #{numero_viaje} con pasajeros:")
    for tipo, nombre in pasajeros:
        print(f"- {nombre} ({tipo})")
        generar_ticket(nombre, tipo, numero_viaje)
        total_atendidos += 1
        if tipo == "General":
            atendidos_general += 1
        elif tipo == "Prioridad":
            atendidos_prioridad += 1
        elif tipo == "Discapacidad":
            atendidos_discapacidad += 1

    for t in range(DURACION_VIAJE):
        print(f"  Turno {t + 1}/{DURACION_VIAJE}")
        time.sleep(espera_turno)

    print("✅ ¡Viaje finalizado!")


def mostrar_estadisticas():
    print("\n📊 ESTADÍSTICAS FINALES 📊")
    print(f"Viajes realizados: {viajes_realizados}")
    print(f"Total de personas atendidas: {total_atendidos}")
    print(f"- General: {atendidos_general}")
    print(f"- Prioridad: {atendidos_prioridad}")
    print(f"- Discapacidad: {atendidos_discapacidad}")
    if viajes_realizados > 0:
        promedio = total_atendidos / viajes_realizados
        print(f"Promedio de personas por viaje: {promedio:.2f}")
    else:
        print("No se realizaron viajes.")


def configurar_tiempo():
    global espera_turno
    try:
        nuevo_tiempo = float(input("¿Cuántos segundos debe durar cada turno del viaje?: "))
        if nuevo_tiempo >= 0:
            espera_turno = nuevo_tiempo
            print(f"Tiempo de espera por turno actualizado a {espera_turno} segundos.")
        else:
            print("El tiempo debe ser un número positivo.")
    except ValueError:
        print("Entrada inválida. No se actualizó el tiempo.")


# ---------- MENÚ PRINCIPAL ----------
def menu_simulador():
    global viajes_realizados

    while True:
        print("\n🎡 MENÚ - Simulador de Parque de Diversiones 🎡")
        print("1. Agregar visitante")
        print("2. Ver estado de las colas")
        print("3. Simular viaje")
        print("4. Configurar tiempo de espera entre turnos")
        print("5. Ver estadísticas y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_visitante_manual()
        elif opcion == "2":
            mostrar_colas()
        elif opcion == "3":
            if len(cola_discapacidad) + len(cola_prioritaria) + len(cola_general) >= CAPACIDAD_VAGON:
                pasajeros = cargar_vagon()
                viajes_realizados += 1
                simular_viaje(pasajeros, viajes_realizados)
            else:
                print("❌ No hay suficientes personas para iniciar un viaje (mínimo 4).")
        elif opcion == "4":
            configurar_tiempo()
        elif opcion == "5":
            mostrar_estadisticas()
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el simulador con menú
menu_simulador()
