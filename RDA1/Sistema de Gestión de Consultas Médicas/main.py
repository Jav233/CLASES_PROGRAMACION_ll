from funciones import registrar_paciente, mostrar_paciente, registrar_consulta, historial_consulta, historial_consulta_general

def menu():
    while True:
        print("----- Sistema de Gestión de Consultas Médicas -----")
        print("1. Registrar un nuevo paciente.")
        print("2. Registrar una consulta médica a un paciente existente.")
        print("3. Mostrar los datos completos de un paciente (incluyendo su historial de consultas).")
        print("4. Mostrar todos los pacientes registrados.")
        print("5. Salir del sistema.")

        opcion = int(input("Seleccione una opción: "))
        
        while opcion < 0 or opcion > 5:
            print("Opción no válida. Intente de nuevo.")
            opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("Bienvenido...")
            print("Registrar un nuevo paciente.")
            registrar_paciente()
        elif opcion == 2:
            registrar_consulta()
        elif opcion == 3:
            print("Mostrar los datos completos de un paciente")
            historial_consulta()
            #mostrar_consultas()
        elif opcion == 4:
            print("Mostrar todos los pacientes registrados")
            historial_consulta_general()
        elif opcion == 5:
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break


# Ejecutar menú
if __name__ == "__main__":
    menu()