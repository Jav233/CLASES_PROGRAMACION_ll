from libro import Libro

libros = []

def registrar_libro():
    print("Registrar un nuevo libro.")
    titulo = input("Ingrese el título del libro: ").capitalize()
    autor = input("Ingrese el autor del libro: ").capitalize()
    #ISBN = int(input("Ingrese el ISBN del libro: "))
    while True:
        ISBN = input("Ingrese el ISBN del libro: ")
        if ISBN.isdigit() :
            # Verificar si el ISBN es un número entero:
            ISBN = int(ISBN)
            while no_repetir_ISBN(ISBN):
                print("El ISBN ya está registrado. Intente de nuevo.")
                ISBN = int(input("Ingrese el ISBN del libro: "))
            break
        
        else:
            print("El ISBN debe ser un número entero. Intente de nuevo.")

    genero = input("Ingrese el género del libro: ").capitalize()
    lista_de_prestamos = []  # Inicializar la lista de préstamos como vacía

    nuevo_libro = Libro(titulo, autor, ISBN, genero, lista_de_prestamos)
    libros.append(nuevo_libro)
    print(f"Libro '{titulo}' registrado exitosamente.\n")

def buscar_libro(ISBN):
    for libro in libros:
        if libro.ISBN == ISBN:
            return libro
    return None

def no_repetir_ISBN(ISBN):
    for libro in libros:
        if libro.ISBN == ISBN:
            return True
    return False

def registrar_prestamo():
    print("Registrar un préstamo.")
    try:
        ISBN = int(input("Ingrese el ISBN del libro: "))
    except ValueError:
        print("El ISBN debe ser un número entero. Intente de nuevo.")
        return
    libro = buscar_libro(ISBN)
    
    if libro:
        print(f"Libro encontrado: {libro.titulo}")
        nombre_prestatario = input("Ingrese el nombre del prestatario: ").capitalize()
        fecha_prestamo = input("Ingrese la fecha de préstamo (DD/MM/AAAA): ")
        libro.lista_de_prestamos.append((nombre_prestatario, fecha_prestamo))
        print(f"Préstamo registrado exitosamente para el libro '{libro.titulo}'.\n")
    else:
        print("El libro no está registrado en el sistema.\n")

def mostrar_informacion_libro():
    print("Mostrar información de un libro.")
    try:
        ISBN = int(input("Ingrese el ISBN del libro: "))
    except ValueError:
        print("El ISBN debe ser un número entero. Intente de nuevo.")
        return
    libro = buscar_libro(ISBN)
    if libro:
        libro.mostrar_detalle()
        cont = 1
        for prestamo in libro.lista_de_prestamos:
            print(f"Préstamo {cont}:")
            print(f"Nombre del prestatario: {prestamo[0]}")
            print(f"Fecha de préstamo: {prestamo[1]}")
            print("----------------------------------")
            cont += 1
    else:
        print("El libro no está registrado en el sistema.\n")

def mostrar_todos_los_libros_registrados():
    print("Mostrar todos los libros registrados.")
    if len(libros) == 0:
        print("No hay libros registrados en el sistema.")
    else:
        for libro in libros:
            libro.mostrar_detalle()
            print("----------------------------------")
            #print(f"Lista de Préstamos: {libro.lista_de_prestamos}")
            cont = 1
            for prestamo in libro.lista_de_prestamos:
                print(f"Préstamo {cont}:")
                print(f"Nombre del libro: {libro.titulo}")
                print(f"ISBN: {libro.ISBN}")
                print(f"Nombre del prestatario: {prestamo[0]}")
                print(f"Fecha de préstamo: {prestamo[1]}")
                print("----------------------------------")
                cont += 1
        print("Total de libros registrados:", len(libros))
        print("----------------------------------\n")
            


