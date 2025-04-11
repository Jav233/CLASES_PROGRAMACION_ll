def emeneses():
    print("Hola Edison como estas")

emeneses()
print("\n")

def funcion(nombre):#Parametro
    print("Estamos estudiando Python", nombre)#Argumento lo que va en el parametro o el valor que va a llevar
funcion('Edison')#Argumento
print("\n")

def datos(nombre, apellido):
    print("Estamos estudiando Python", nombre, apellido)
datos('Edison', 'Emeneses')#Argumento posicional
datos(nombre='Edison', apellido='Emeneses')#Argumento nominal
print("\n")

print("Retorno de una fumcion")
def area_triangulo(base, altura):
    calc = base * altura/2
    print(calc)
area_triangulo(2,3)
area_triangulo(4,5)
print("\n")

print("Argumentos por defecto")
def welcome(nombre, lenguaje='Python', lengua = 'Program'):#Preestablecido su argumento
    print('!Bienvenidosa', lenguaje, lengua, nombre + '!')
welcome('Emeneses')
welcome('Emeneses', 'PHP')
welcome('Emeneses', 'HTML', 'Programacion')
#welcome() Errores
#welcome('Emeneses', 'Python', 'Program', 'Extra') Error
print("\n")

print("Pasar un numero indeterminado de argumentos")
def menu(*platos):#El asterisco me crea un lista de parametros
    print('Hoy tenemos: ', end='')
    for plato in platos:
        print(plato, end=', ')
menu('pasta', 'pizza', 'ensalada')
print("\n")

#**parametro clave : valor
def contacto(**info):
    print("Datos del contacto")
    for clave, valor in info.items():#item (Clave y valor)
        print(clave,":", valor)
contacto(Nombre = 'Emeneses', Email = 'emeneses@emenesesdevelopers.com')
print("\n")
contacto(Nombre = 'Emeneses', Email = 'emeneses@emenesesdevelopers.com', Direccion = 'Quito-Ecuador')
print("\n")


print("Las funciones son objetos")
#ojo ojo ojo
def saludo(nombre):
    print('Hola como estas', nombre)
    return
bienvenido = saludo
bienvenido('Emeneses')
print('\n')

print("Funciones recursivas")
def cuenta_recursiva(numero):
    numero -=1
    if numero > 0:
        print(numero)
        cuenta_recursiva(numero)
    else:
        print("Boooooooooooom")
    print("Fin de la funcion", numero)
cuenta_recursiva(numero=5) 
print("\n")

# print("Funcion recursiva con retorno")
# def factorial(numero):
#     print("Valor inicial -> ", numero)
#     if numero >1:

class Persona:
    def __init__(self, nombre, edad, ocupacion): #init es un metodo inicializacion de atributos
        self.nombre = nombre #self 
        self.edad = edad
        self.ocupacion = ocupacion
    
    def mostrar_detalle(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"
#Creamos objetos de tipo persona
persona1 = Persona('Juan', 30, 'Desarrollador') #Objetos
persona2 = Persona('Pedro', 25, 'Estudiante')

#Mostramos la descripcion de cada persona
print(persona1.mostrar_detalle())
print(persona2.mostrar_detalle())

# class Persona:
#     def __init__(self, nombre, edad, ocupacion):
#         self.nombre = nombre      #En self vamos almacenar todos lo parametros que tenemos en el metodo
#         self.edad = edad
#         self.ocupacion = ocupacion
#     def mostrar_detalle(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"

# #Pedimos al usuario que ingrese informacion para crear objetos Persona
# nombre = input("Ingrese su nombre: ").capitalize()
# edad = int(input("Ingrese su edad: "))
# ocupacion = input("Ingrese su ocupacion: ").capitalize()
# #Creamos un objeto Persona con la informacion ingresada por el usuario
# nueva_persona = Persona(nombre, edad, ocupacion)
# #Mostramos la descripcion de la nueva persona
# print("\n Informacion de la persona creada")
# print(nueva_persona.mostrar_detalle())

#programa
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"

def mostrar_menu():
    print("\n ------ Gestion de Personas ------")
    print("1. Agregar Personas")
    print("2. Mostrar todas las personas")
    print("3. Buscar Persona por nombre")
    print("4. Salir")
    
personas = []

while True:
    mostrar_menu()
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        ocupacion = input("Ingrese su ocupacion: ")
        nueva_persona = Persona(nombre, edad, ocupacion)
        personas.append(nueva_persona)
        print(f"La persona '{nombre}' ha sido agregada")
        
    elif opcion == "2":
        if len(personas)>0:
            print("\n --- Lista de personas ---")
            for persona in personas:
                print(persona.descripcion())
        else:
            print("No hay personas en la lista")
    
    elif opcion == "3":
        if len(personas) > 0:
            nombre_buscar = input("Ingrese el nombre de la persona a buscar: ").capitalize()
            encontrado = False
            for persona in personas:
                if persona.nombre.lower() == nombre_buscar.lower():
                    print("Persona encontrada")
                    print(persona.descripcion())
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontri a '{nombre_buscar}' en la lista")
            else:
                print("No hay personas en la lista")
    elif opcion == '4':
        print("Gracias por utilizar el sistema")
        break
    else:
        print("Opcion invalida, por favor seleccione una opcion valida")
