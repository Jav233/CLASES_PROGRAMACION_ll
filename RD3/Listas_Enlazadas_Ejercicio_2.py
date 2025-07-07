# Clase que representa un nodo doblemente enlazado
class ListaAtencion:
    def __init__(self, dato):
        self.dato = dato           # URL o página que se visita
        self.siguiente = None     # Enlace al siguiente nodo
        self.anterior = None      # Enlace al nodo anterior

# Clase que gestiona el historial de navegación
class HistorialNavegacion:
    def __init__(self):
        self.actual = None        # Página actual
        self.inicio = None        # Primera página del historial

    # Método para visitar una nueva página
    def visitar_pagina(self, url):
        nuevo_nodo = ListaAtencion(url)  # Se crea un nuevo nodo con la URL
        if self.actual:
            # Si hay una página actual, se enlaza el nuevo nodo después de ella
            self.actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.actual
        else:
            # Si no hay historial, esta será la primera página
            self.inicio = nuevo_nodo
        # Se actualiza la página actual al nuevo nodo
        self.actual = nuevo_nodo

    # Método para retroceder una página en el historial
    def atras(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            print("No hay páginas anteriores.")

    # Método para avanzar una página en el historial
    def adelante(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            print("No hay páginas siguientes.")

    # Método para mostrar todo el historial de navegación
    def mostrar_historial(self):
        nodo = self.inicio
        print("\nHistorial de navegación:")
        while nodo:
            if nodo == self.actual:
                marca = "  <-- Página actual"
            else:
                marca = ""
            print("- " + str(nodo.dato) + marca)
            nodo = nodo.siguiente

    # Método para mostrar la página actual
    def pagina_actual(self):
        if self.actual:
            return self.actual.dato
        else:
            return "No hay páginas visitadas."

    # Método para insertar una nueva página al principio del historial
    def insertar_pagina(self, url):
        nuevo_nodo = ListaAtencion(url)
        if not self.inicio:
            # Si el historial está vacío, se asigna como primera y actual
            self.inicio = nuevo_nodo
            self.actual = nuevo_nodo
        else:
            # Enlaza el nuevo nodo como el primero del historial
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo
            self.actual = nuevo_nodo  # También se actualiza la página actual

    # Método para eliminar una página específica del historial
    def eliminar_pagina(self, url):
        nodo = self.inicio
        while nodo:
            if nodo.dato == url:
                # Enlazar los nodos anterior y siguiente para eliminar el nodo actual
                if nodo.anterior:
                    nodo.anterior.siguiente = nodo.siguiente
                else:
                    self.inicio = nodo.siguiente  # Si se elimina el primero

                if nodo.siguiente:
                    nodo.siguiente.anterior = nodo.anterior

                # Si se elimina la página actual, se actualiza el puntero actual
                if nodo == self.actual:
                    self.actual = nodo.anterior or nodo.siguiente
                return
            nodo = nodo.siguiente
        print("Página no encontrada en el historial.")

# Ejemplo de uso del historial
nav = HistorialNavegacion()
nav.visitar_pagina("google.com")
nav.visitar_pagina("openai.com")
nav.visitar_pagina("github.com")
nav.visitar_pagina("python.org")
nav.visitar_pagina("wikipedia.org")

nav.atras()  # Retrocede una página (a "python.org")
nav.mostrar_historial()  # Muestra el historial actual

nav.eliminar_pagina("openai.com")  # Elimina "openai.com" del historial
nav.mostrar_historial()  # Muestra el historial después de eliminar

nav.insertar_pagina("stackoverflow.com")  # Inserta "stackoverflow.com" al inicio
nav.mostrar_historial()  # Muestra el historial actualizado
