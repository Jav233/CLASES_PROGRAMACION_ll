from paciente import Paciente

pacientes = []

def registrar_paciente():
    nome = input("Ingrese su nombre: ").capitalize()
    
    cedula = input("Ingrese su Cédula: ")
    while repetir_cedula(cedula):
        print("La cédula ya está registrada. Intente de nuevo.")
        cedula = input("Ingrese su Cédula: ")
    
    while True:
        if validar_cedula(cedula):
            break
        else:
            print("La cédula no es válida. Intente de nuevo.")
            cedula = input("Ingrese su Cédula: ")

    edad = int(input("Ingrese su Edad: "))
    while edad <= 0 or edad > 120:
        print("Edad no válida. Debe ser un número entre 1 y 120.")
        edad = int(input("Ingrese su Edad: "))
    
    #tipo_de_sangre = input("Ingrese su Tipo de Sangre: ").upper()
    
    tipos_validos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    while True:
        tipo_de_sangre = input("Ingrese su Tipo de Sangre: ").upper()
        
        encontrado = False
        for tipo in tipos_validos:
            if tipo == tipo_de_sangre:
                encontrado = True
                break
        if encontrado == True:
            break
        else:
            print("Tipo de sangre no válido. Debe ser A+, A-, B+, B-, AB+, AB-, O+ u O-.")
        
    paciente_ingreso = Paciente(nome, cedula, edad, tipo_de_sangre)
    pacientes.append(paciente_ingreso)
    print("Paciente registrado con éxito.\n")

def buscar_paciente(cedula):
    for paciente in pacientes:
        if paciente.cedula == cedula:
            
            return paciente
    return None

def repetir_cedula(cedula):
    for paciente in pacientes:
        if paciente.cedula == cedula:
            return True
    return False

def mostrar_paciente():
    cedula = input("Ingrese la cédula del paciente: ")
    paciente = buscar_paciente(cedula)
    if paciente:
        paciente.mostrar_detalle()
    else:
        print("Paciente no encontrado.\n")

def registrar_consulta():
    cedula = input("Ingrese la cédula del paciente: ")
    paciente = buscar_paciente(cedula)
    if paciente:
        print(f"Paciente: {paciente.nombre}")
        fecha = input("Fecha de la consulta (dd/mm/aaaa): ")
        motivo = input("Motivo de la consulta: ").capitalize()
        diagnostico = input("Diagnóstico: ").capitalize()
        tratamiento = input("Tratamiento: ").capitalize()
        paciente.historial_consultas.append([fecha, motivo, diagnostico, tratamiento])
        print("Consulta registrada con éxito.\n")
    else:
        print("Paciente no encontrado.\n")


    
#Validar cedula
def validar_cedula(cedula):
    # Verificar que tenga solo dígitos
    if not cedula.isdigit():
        print("La cédula debe contener solo números.")
        return False

    # Verificar longitud
    if len(cedula) != 10:
        print("La cédula debe tener exactamente 10 dígitos.")
        return False

    # Validar código de provincia
    provincia = int(cedula[:2])
    if provincia < 1 or provincia > 24:
        print("Código de provincia inválido. Debe estar entre 1 y 24.")
        return False

    return True 

def historial_consulta():
    cedula = input("Ingrese la cédula del paciente: ")
    paciente = buscar_paciente(cedula)
    if paciente:
        print(f"\nPaciente: {paciente.nombre}")
        print("Historial de consultas:")
        if paciente.historial_consultas:
            contador = 1
            for consulta in paciente.historial_consultas:
                print(f"\nConsulta #{contador}")
                print(f"Fecha      : {consulta[0]}")
                print(f"Motivo     : {consulta[1]}")
                print(f"Diagnóstico: {consulta[2]}")
                print(f"Tratamiento: {consulta[3]}")
                print("-" * 40)
                contador += 1
        else:
            print("No hay consultas registradas.")
    else:
        print("Paciente no encontrado.\n")


def historial_consulta_general():
    if pacientes:
        print("\n======= HISTORIAL COMPLETO DE CONSULTAS =======\n")
        for paciente in pacientes:
            print(f"Paciente: {paciente.nombre} | Cédula: {paciente.cedula}")
            if paciente.historial_consultas:
                contador = 1
                for consulta in paciente.historial_consultas:
                    print(f"\nConsulta #{contador}")
                    print(f"Fecha      : {consulta[0]}")
                    print(f"Motivo     : {consulta[1]}")
                    print(f"Diagnóstico: {consulta[2]}")
                    print(f"Tratamiento: {consulta[3]}")
                    print("-" * 40)
                    contador += 1
            else:
                print("Sin consultas registradas.")
            print("=" * 50)
    else:
        print("No hay pacientes registrados.\n")
