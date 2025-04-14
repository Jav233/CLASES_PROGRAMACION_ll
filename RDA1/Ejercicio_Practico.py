# class Libro:
#     def __init__(self, titulo, autor, anio_publicacion):
#         self.titulo = titulo
#         self.autor = autor
#         self.anio_publicacion = anio_publicacion
    
#     def descripcion(self):
#         return f"Titulo: {self.titulo}, Autor: {self.autor}, Año de Publicacion: {self.anio_publicacion}"

# Libros = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
# print(Libros.descripcion())


class Estudiante:
    def __init__(self, nombre, carrera, nota_final ):
        self.nombre = nombre
        self.carrera = carrera
        self.nota_final = nota_final

    def calcular_aprobacion(self):
        if self.nota_final >= 7:
            return "Aprobado"
        else:
            return "Desaprobado"
    
    # def mostrar_detalle(self):
    #     return f"Nombre: {self.nombre}, Carrera: {self.carrera}, Nota: {self.nota_final}, Estado: {self.calcular_aprobacion()}"
    
Estudiante1 = Estudiante("Juan", "Ingenieria", 8.5)
Estudiante2 = Estudiante("Maria", "Arquitectura", 6.5)

# print(Estudiante1.mostrar_detalle())
# print(Estudiante2.mostrar_detalle())

print(Estudiante1.nombre, Estudiante1.carrera ,Estudiante1.nota_final, Estudiante1.calcular_aprobacion())
print(Estudiante2.nombre, Estudiante2.carrera ,Estudiante2.nota_final, Estudiante2.calcular_aprobacion())

######################################################################
class Vehiculo:
    def moverse(self):
        print("El vehiculo se mueve")

class Auto(Vehiculo):
    def mover(self):
        print("El auto se mueve")

carro = Auto()
carro.mover()
##################################################################

class Pajaro :
    def sonido(self):
        print("El pajaro canta")

class Gato:
    def sonido(self):
        print("El gato maulla")

def hacer_sonido(animal):
    animal.sonido()

gato = Gato()
pajaro = Pajaro()

hacer_sonido(gato)
hacer_sonido(pajaro)
###################################################################
