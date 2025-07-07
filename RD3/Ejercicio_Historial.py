# Definición del nodo doblemente enlazado
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato            # Almacena la URL de la página
        self.anterior = None       # Apunta al nodo anterior en el historial
        self.siguiente = None      # Apunta al nodo siguiente en el historial

# Clase principal que maneja el historial del navegador
class HistorialNavegador:
    def __init__(self):
        self.actual = None  # Nodo donde se encuentra el usuario actualmente

    # Método para visitar una nueva página
    def visitar_pagina(self, url):
        nuevo_nodo = NodoDoble(url)  # Creamos un nuevo nodo con la URL
        if self.actual:
            # Si ya hay una página actual, eliminamos el "futuro"
            self.actual.siguiente = None  # Desconectamos las páginas siguientes
            nuevo_nodo.anterior = self.actual  # El nuevo nodo apunta al actual
            self.actual.siguiente = nuevo_nodo  # El nodo actual apunta al nuevo
        self.actual = nuevo_nodo  # El nuevo nodo se convierte en la página actual

    # Método para retroceder en el historial
    def atras(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior  # Vamos al nodo anterior
        else:
            print("No hay páginas anteriores.")  # Ya estamos al inicio del historial

    # Método para avanzar en el historial (si se retrocedió antes)
    def adelante(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente  # Vamos al nodo siguiente
        else:
            print("No hay páginas siguientes.")  # Ya estamos al final del historial

    # Método para mostrar el historial completo desde el inicio hasta la página actual
    def mostrar_historial(self):
        # Ir al principio del historial
        nodo = self.actual
        while nodo and nodo.anterior:
            nodo = nodo.anterior  # Retrocedemos hasta el primer nodo

        print("\nHistorial de navegación:")
        while nodo:
            # Marcamos la página actual
            if nodo == self.actual:
                marca = "  <-- Página actual"
            else:
                marca = ""

            print("- " + str(nodo.dato) + marca)
            nodo = nodo.siguiente  # Avanzamos al siguiente nodo

    # Método para obtener la URL de la página actual
    def pagina_actual(self):
        if self.actual:
            return self.actual.dato
        else:
            return "No hay páginas visitadas."

# Creamos una instancia del historial
nav = HistorialNavegador()

# Visitamos tres páginas seguidas
nav.visitar_pagina("google.com")
nav.visitar_pagina("openai.com")
nav.visitar_pagina("github.com")

# Retrocedemos dos veces en el historial (ahora estamos en "google.com")
nav.atras()
nav.atras()

# Visitamos una nueva página, esto borra el "futuro" (openai y github)
nav.visitar_pagina("stackoverflow.com")

# Mostramos el historial desde el inicio hasta la página actual
nav.mostrar_historial()

# Mostramos la URL actual
print("Página actual:", nav.pagina_actual())
