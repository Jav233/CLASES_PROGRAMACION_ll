# Clase ReporteMedico, que también funcionará como nodo de la pila
class ReporteMedico:
    def __init__(self, tipo, observacion):
        self.tipo = tipo  # Tipo del reporte (por ejemplo: "Fractura", "Dolor de cabeza")
        self.observacion = observacion  # Descripción u observación del caso
        self.siguiente = None  # Puntero al siguiente reporte (nodo anterior en la pila)

# Clase PilaReportes que maneja una pila de objetos ReporteMedico
class PilaReportes:
    def __init__(self):
        self.cabeza = None  # Representa el tope de la pila

    def agregar_reporte(self, tipo, observacion):
        # Creamos un nuevo reporte médico (este será el nuevo nodo también)
        nuevo_reporte = ReporteMedico(tipo, observacion)
        
        # El siguiente del nuevo reporte apunta al actual tope de la pila
        nuevo_reporte.siguiente = self.cabeza
        
        # El nuevo reporte ahora se convierte en el tope de la pila
        self.cabeza = nuevo_reporte

        print(f"Reporte de tipo '{tipo}' agregado con observación: '{observacion}'")
        return nuevo_reporte

    def eliminar_reporte(self):
        if self.cabeza is None:
            # Si la pila está vacía, no hay nada que eliminar
            print("No hay reportes para eliminar.")
            return None
        
        # Guardamos el nodo que se va a eliminar
        reporte_eliminado = self.cabeza
        
        # Movemos el tope de la pila al siguiente nodo
        self.cabeza = self.cabeza.siguiente

        print(f"Reporte de tipo '{reporte_eliminado.tipo}' eliminado.")
        return reporte_eliminado

    def mostrar_reportes(self):
        if self.cabeza is None:
            print("La pila está vacía.")
        else:
            actual = self.cabeza  # Comenzamos desde el tope de la pila
            print("Reportes en la pila (del más reciente al más antiguo):")
            while actual:
                # Mostramos cada reporte
                print(f"- Tipo: {actual.tipo}, Observación: {actual.observacion}")
                actual = actual.siguiente  # Pasamos al siguiente nodo

    def esta_vacia(self):
        # Devuelve True si la pila está vacía
        return self.cabeza is None
    
#Ejemplo
pila = PilaReportes()
pila.agregar_reporte("Consulta", "Dolor de cabeza")
pila.agregar_reporte("Seguimiento", "Revisión de síntomas")
pila.mostrar_reportes()
pila.eliminar_reporte()
pila.mostrar_reportes()



# Clase EstudianteEvacuacion que actúa como nodo en la cola
class EstudianteEvacuacion:
    def __init__(self, nombre, aula):
        self.nombre = nombre         # Nombre del estudiante
        self.aula = aula             # Aula del estudiante
        self.siguiente = None        # Enlace al siguiente estudiante en la cola

# Clase ColaEvacuacion que implementa una cola con punteros (no usa listas)
class ColaEvacuacion:
    def __init__(self):
        self.cabeza = None  # Primer estudiante en la cola (el que será atendido primero)
        self.cola = None    # Último estudiante en la cola (el más recientemente agregado)

    def agregar_estudiante(self, nombre, aula):
        # Creamos un nuevo estudiante (que también actuará como nodo)
        nuevo_estudiante = EstudianteEvacuacion(nombre, aula)

        if self.cabeza is None:
            # Si la cola está vacía, el nuevo estudiante es cabeza y cola
            self.cabeza = nuevo_estudiante
            self.cola = nuevo_estudiante
        else:
            # Si la cola no está vacía, agregamos al final
            self.cola.siguiente = nuevo_estudiante
            self.cola = nuevo_estudiante

        print(f"Estudiante '{nombre}' agregado a la cola de evacuación desde el aula '{aula}'.")
        return nuevo_estudiante

    def atender_estudiante(self):
        if self.cabeza is None:
            # No hay estudiantes para atender
            print("No hay estudiantes en la cola de evacuación.")
            return None

        # Tomamos al primer estudiante (el que está en cabeza)
        estudiante_atendido = self.cabeza

        # Movemos la cabeza al siguiente estudiante
        self.cabeza = self.cabeza.siguiente

        # Si después de atender no queda nadie, actualizamos también la cola
        if self.cabeza is None:
            self.cola = None

        print(f"Estudiante '{estudiante_atendido.nombre}' atendido desde el aula '{estudiante_atendido.aula}'.")
        return estudiante_atendido

    def mostrar_en_espera(self):
        if self.cabeza is None:
            print("La cola de evacuación está vacía.")
        else:
            actual = self.cabeza
            print("Estudiantes en espera de evacuación:")
            while actual:
                # Mostramos el estudiante actual
                print(f"- Nombre: {actual.nombre}, Aula: {actual.aula}")
                actual = actual.siguiente  # Avanzamos al siguiente estudiante

    def esta_vacia(self):
        # Devuelve True si no hay estudiantes en la cola
        return self.cabeza is None

#Ejemplo
cola = ColaEvacuacion()
cola.agregar_estudiante("Juan Pérez", "Aula 101")
cola.agregar_estudiante("María López", "Aula 102")
cola.agregar_estudiante("Pedro Gómez", "Aula 103")
cola.mostrar_en_espera()
cola.atender_estudiante()
cola.mostrar_en_espera()


# Clase que representa una visita médica de un estudiante
class VisitaMedica:
    def __init__(self, estudiante, motivo, fecha):
        self.estudiante = estudiante  # Nombre del estudiante
        self.motivo = motivo          # Motivo de la visita médica
        self.fecha = fecha            # Fecha de la visita

# Clase NodoDoble para lista doblemente enlazada
class NodoDoble:
    def __init__(self, visita):
        self.visita = visita          # Contiene un objeto de tipo VisitaMedica
        self.anterior = None          # Referencia al nodo anterior en la lista
        self.siguiente = None         # Referencia al nodo siguiente en la lista

# Clase que administra la lista doblemente enlazada de visitas médicas
class ListaVisitas:
    def __init__(self):
        self.actual = None  # Puntero al nodo actual (última visita agregada o donde se navega)

    # Método para agregar una nueva visita médica al inicio de la lista
    def agregar_visita(self, estudiante, motivo, fecha):
        nueva_visita = VisitaMedica(estudiante, motivo, fecha)  # Crear una nueva visita
        if self.actual is None:
            # Si la lista está vacía, el nuevo nodo es el único nodo
            self.actual = NodoDoble(nueva_visita)
        else:
            # Si ya hay elementos, enlazamos el nuevo nodo antes del actual
            nuevo_nodo = NodoDoble(nueva_visita)
            nuevo_nodo.siguiente = self.actual     # El nuevo nodo apunta al actual
            self.actual.anterior = nuevo_nodo      # El actual apunta hacia atrás al nuevo
            self.actual = nuevo_nodo               # Actualizamos el puntero actual
        print(f"Visita médica agregada para el estudiante '{estudiante}' con motivo '{motivo}' en la fecha '{fecha}'.")

    # Método para retroceder en la lista (ir al nodo anterior)
    def retroceder(self):
        if self.actual is None:
            print("No hay visitas médicas registradas.")
            return None
        if self.actual.anterior is None:
            print("No se puede retroceder más, ya estás en la primera visita.")
            return None
        self.actual = self.actual.anterior  # Retrocedemos una visita
        print(f"Retrocediendo a la visita médica del estudiante '{self.actual.visita.estudiante}' con motivo '{self.actual.visita.motivo}' en la fecha '{self.actual.visita.fecha}'.")

    # Método para avanzar en la lista (ir al nodo siguiente)
    def avanzar(self):
        if self.actual is None:
            print("No hay visitas médicas registradas.")
            return None
        if self.actual.siguiente is None:
            print("No se puede avanzar más, ya estás en la última visita.")
            return None
        self.actual = self.actual.siguiente  # Avanzamos una visita
        print(f"Avanzando a la visita médica del estudiante '{self.actual.visita.estudiante}' con motivo '{self.actual.visita.motivo}' en la fecha '{self.actual.visita.fecha}'.")

    # Mostrar los datos de la visita médica en la posición actual
    def mostrar_actual(self):
        if self.actual is None:
            print("No hay visitas médicas registradas.")
            return None
        visita = self.actual.visita
        print(f"Visita médica actual: Estudiante: {visita.estudiante}, Motivo: {visita.motivo}, Fecha: {visita.fecha}")
        return visita

    # Verifica si la lista está vacía
    def esta_vacia(self):
        return self.actual is None

# Pruebas de la clase ListaVisitas
lista_visitas = ListaVisitas()
# Agregamos algunas visitas médicas
lista_visitas.agregar_visita("Ana Torres", "Chequeo general", "2023-10-01")
lista_visitas.agregar_visita("Juan Pérez", "Vacuna", "2023-10-02")
# Agregamos más visitas
lista_visitas.agregar_visita("María López", "Consulta de alergias", "2023-10-03")
# Avanzamos y retrocedemos en la lista
lista_visitas.mostrar_actual()  # Muestra la última visita agregada
lista_visitas.avanzar()  # No debería avanzar, ya que es la última visita
lista_visitas.retroceder()  # Retrocede a la visita de Juan Pérez


# Clase Incidente: representa un evento registrado en la bitácora
class Incidente:
    def __init__(self, anio, tipo):
        self.anio = anio      # Año en el que ocurrió el incidente
        self.tipo = tipo      # Tipo de incidente (por ejemplo, "terremoto", "inundación")

# Clase NodoIncidente: representa un nodo de la lista enlazada simple
class NodoIncidente:
    def __init__(self, incidente):
        self.incidente = incidente  # Objeto Incidente almacenado en el nodo
        self.siguiente = None       # Puntero al siguiente nodo en la lista

# Clase ListaBitacora: maneja la lista enlazada simple de incidentes
class ListaBitacora:
    def __init__(self):
        self.inicio = None  # Puntero al primer nodo de la lista (cabeza)

    # Agrega un nuevo incidente al inicio de la lista
    def agregar_incidente(self, anio, tipo):
        nuevo_incidente = Incidente(anio, tipo)             # Crea el objeto incidente
        nuevo_nodo = NodoIncidente(nuevo_incidente)         # Crea el nodo que lo envuelve

        if self.inicio is None:
            self.inicio = nuevo_nodo  # Si la lista está vacía, ese nodo es el primero
        else:
            nuevo_nodo.siguiente = self.inicio  # Enlaza el nuevo nodo al inicio actual
            self.inicio = nuevo_nodo            # Actualiza el inicio con el nuevo nodo

        print(f"Incidente de tipo '{tipo}' del año {anio} agregado a la bitácora.")
        return nuevo_incidente

    # Elimina un incidente de la lista según el año
    def eliminar_incidente(self, anio):
        if self.inicio is None:
            print("No hay incidentes registrados para eliminar.")
            return None

        actual = self.inicio

        # Caso especial: el incidente a eliminar está en el primer nodo
        if actual.incidente.anio == anio:
            self.inicio = actual.siguiente
            print(f"Incidente de tipo '{actual.incidente.tipo}' del año {anio} eliminado de la bitácora.")
            return actual.incidente

        # Recorre la lista buscando el nodo a eliminar
        while actual.siguiente:
            if actual.siguiente.incidente.anio == anio:
                eliminado = actual.siguiente
                actual.siguiente = eliminado.siguiente  # Saltamos el nodo eliminado
                print(f"Incidente de tipo '{eliminado.incidente.tipo}' del año {anio} eliminado de la bitácora.")
                return eliminado.incidente
            actual = actual.siguiente

        # Si se recorre toda la lista sin encontrar el incidente
        print("No se encontró ningún incidente para eliminar.")
        return None

    # Busca un incidente por año
    def buscar_incidente(self, anio):
        if self.inicio is None:
            print("No hay incidentes registrados.")
            return None

        actual = self.inicio

        # Recorre la lista hasta encontrar el incidente o llegar al final
        while actual:
            if actual.incidente.anio == anio:
                print(f"Incidente encontrado: Tipo: {actual.incidente.tipo}, Año: {actual.incidente.anio}")
                return actual.incidente
            actual = actual.siguiente

        print(f"No se encontró ningún incidente del año {anio}.")
        return None

    # Verifica si la lista está vacía
    def esta_vacia(self):
        return self.inicio is None

    # Muestra todos los incidentes registrados en la lista
    def mostrar_incidentes(self):
        if self.inicio is None:
            print("No hay incidentes registrados.")
            return

        actual = self.inicio
        print("Incidentes registrados:")
        while actual:
            print(f"- Tipo: {actual.incidente.tipo}, Año: {actual.incidente.anio}")
            actual = actual.siguiente

# Pruebas de la clase ListaBitacora
bitacora = ListaBitacora()
# Agregamos algunos incidentes
bitacora.agregar_incidente(2020, "terremoto")
bitacora.agregar_incidente(2021, "inundación")
bitacora.agregar_incidente(2022, "incendio forestal")
bitacora.agregar_incidente(2023, "huracán")
# Mostramos todos los incidentes registrados
bitacora.mostrar_incidentes()
# Eliminamos un incidente específico
bitacora.eliminar_incidente(2021)  # Elimina el incidente de inundación del año 2021
# Mostramos los incidentes después de la eliminación
bitacora.mostrar_incidentes()


