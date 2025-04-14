# class Persona_imput:
#     def __init__(self): #init es un metodo inicializacion de atributos
#         self.nombre = input("Ingrese su nombre: ") #Atributos de la clase
#         self.edad = int(input("Ingrese su edad: "))
#         self.ocupacion = input("Ingrese su ocupacion: ")
    
#     def mostrar_detalle(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"
# #Creamos objetos de tipo persona
# # persona1 = Persona_imput() #Objetos
# # print(persona1.mostrar_detalle())

# def mostrar_menu():
#     print("\n ------ Gestion de Personas ------")
#     print("1. Agregar Personas")
#     print("2. Mostrar todas las personas")
#     print("3. Buscar Persona por nombre")
#     print("4. Salir")
    
# personas = []

# while True:
#     mostrar_menu()
#     opcion = input("Ingrese la opcion que desea realizar: ")
    
#     if opcion == "1":
        
#         print("Agregando nueva persona...")
#         n = int(input("Cuantas personas desea agregar: "))
#         for i in range(n):
#             print(f"Persona {i+1}:")
#             persona = Persona_imput()
#             personas.append(persona)
#             print(f"La persona '{persona.nombre}' ha sido agregada")
        
#     elif opcion == "2":
#         if len(personas)>0:
#             print("\n --- Lista de personas ---")
#             for persona in personas:
#                 print(persona.mostrar_detalle())
#         else:
#             print("No hay personas en la lista")
                
#     elif opcion == "3":
#         nombre = input("Ingrese el nombre de la persona que desea buscar: ")
#         encontrado = False
#         for persona in personas:
#             if persona.nombre == nombre:
#                 if persona.nombre.lower() == nombre.lower():
#                     print("Persona encontrada")
#                     print(persona.descripcion())
#                     encontrado = True
#                     break
#         if not encontrado:
#             print(f"La persona '{nombre}' no se encuentra en la lista")
#     elif opcion == "4":
#         print("Saliendo del programa...")
#         break
#     else:
#         print("Opcion no valida, por favor intente nuevamente")
        
# while True:
#     try:
#         nombre = input("Ingrese su nombre de la persona (o escriba 'salir' para salir): ")
#         if nombre.lower() == "salir":
#             print("Saliendo del programa...")
#             break
#         edad = int(input("Ingrese su edad: "))
#         ocupacion = input("Ingrese su ocupacion: ")
        
#         persona = Persona_imput(nombre, edad, ocupacion)
#         print(persona.descripcion())
        
#     except ValueError:
#         print("Error: La edad debe ser un numero entero. Intente nuevamente.")
#     except KeyboardInterrupt:
#         print("\nSaliendo del programa...")
#         break

# class Perro:
#     def __init__(self, nombre, edad, raza):
#         self.nombre = nombre
#         self.edad = edad
#         self.raza = raza
    
#     def ladrar(self):
#         print("Guau!") 
# #objeto
# perro1 = Perro("Fito", 3, "Labrador")
# print(perro1.nombre)
# perro1.ladrar()

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def ver_saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("Deposito exitoso")

cuenta = CuentaBancaria(1000)
print("Saldo inicial:", cuenta.ver_saldo())
cuenta.depositar(500)
print("Saldo actual:", cuenta.ver_saldo())