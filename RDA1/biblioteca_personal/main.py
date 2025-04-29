from funciones import registrar_libro, registrar_prestamo, mostrar_informacion_libro, mostrar_todos_los_libros_registrados


def menu():
    while True:
        try:
            
            print("----- Sistema de Gestión de Biblioteca Personal -----")
            print("1. Registrar un nuevo libro.")
            print("2. Registrar un préstamo")
            print("3. Mostrar información de un libro.")
            print("4. Mostrar todos los libros.")
            print("5. Salir del sistema.")

            opcion = int(input("Seleccione una opción: "))
            
            while opcion < 0 or opcion > 5:
                print("Opción no válida. Intente de nuevo, solo numeros del 1 al 5.")
                opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                print("----------Bienvenido---------")
                
                registrar_libro()
            elif opcion == 2:
                #print("Registrar un préstamo")
                registrar_prestamo()
            elif opcion == 3:
                #print("Mostrar información de un libro.")
                mostrar_informacion_libro()
            elif opcion == 4:
                #print("Mostrar todos los libros.")
                mostrar_todos_los_libros_registrados()
            elif opcion == 5:
                print("Salir del sistema.")
                break
        except ValueError:
            print("Opción no válida. Intente de nuevo, solo numeros del 1 al 5.")
            continue
        

if __name__ == "__main__":
    menu()