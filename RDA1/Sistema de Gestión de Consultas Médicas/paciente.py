class Paciente:
    def __init__(self, nombre, cedula, edad, tipo_de_sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_de_sangre = tipo_de_sangre
        self.historial_consultas = []
        
    def mostrar_detalle(self):
        print("----- DETALLES DEL PACIENTE -----")
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de Sangre: {self.tipo_de_sangre}")
        print("----------------------------------\n")
    
    