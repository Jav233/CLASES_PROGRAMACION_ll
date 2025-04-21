class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.notas = []
        
    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota {nota} agregada a {self.nombre}")
    
    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0
    
    def estado(self):
        return "APROBADO" if self.promedio() >= 7 else "DESAPROBADO"
    
    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}")
        print(f"Matricula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.promedio():.2f}")
        print(f"Estado: {self.estado()}\n")   
    
    #Lista de guardado de estudiantes
    
estudiantes = []
    
def buscar_estudiante(matricula):
    for est in estudiantes:
        if est.matricula == matricula:
            return est
    return None
    #Menu principal
    
while True:
    print("----- SISTEMA DE REGISTRO DE ESTUDIANTES -----")
    print("1. Registrar nuevo estudiante")
    print("2. Agregar nota a un estudiante")
    print("3. Mostrar datos de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        matricula = input("Matrícula: ")
        carrera = input("Carrera: ")
        estudiante = Estudiante(nombre, matricula, carrera)
        estudiantes.append(estudiante)
        print("Estudiante registrado con éxito.\n")

    elif opcion == "2":
        matricula = input("Ingrese la matrícula del estudiante: ")
        estudiante = buscar_estudiante(matricula)
        if estudiante:
            try:
                nota = float(input("Ingrese la nota: "))
                estudiante.agregar_nota(nota)
                print("Nota agregada con éxito.\n")
            except ValueError:
                print("Nota inválida. Debe ser un número.\n")
        else:
            print("Estudiante no encontrado.\n")

    elif opcion == "3":
        matricula = input("Ingrese la matrícula del estudiante: ")
        estudiante = buscar_estudiante(matricula)
        if estudiante:
            estudiante.mostrar_datos()
        else:
            print("Estudiante no encontrado.\n")

    elif opcion == "4":
        if not estudiantes:
            print("No hay estudiantes registrados.\n")
        for est in estudiantes:
            est.mostrar_datos()

    elif opcion == "5":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intente de nuevo.\n")

