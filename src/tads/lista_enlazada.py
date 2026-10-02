from src.tads.nodo import Nodo

class ListaEnlazada:

    def __init__(self):
        self._cabeza = None
        self._cantidad = 0

    def esta_vacia(self):
        
        if self._cantidad == 0:
            return True
        
        return False

    def tamanio(self):

        return self._cantidad

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo_nodo
        self._cantidad += 1

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.esta_vacia():
            self._cabeza = nuevo_nodo

        else:
            actual = self._cabeza
            while actual.prox is not None:
                actual = actual.prox

            actual.prox = nuevo_nodo

        self._cantidad += 1


    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError

    def eliminar(self, dato):
        
        if self.esta_vacia():
            return print("\n Su lista esta vacía..")
        
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.prox
            self._cantidad -= 1
            return dato

        actual = self._cabeza
        while actual.prox is not None:
            if actual.prox.dato == dato:
                actual.prox = actual.prox.prox
                self._cantidad -= 1
                return
            actual = actual.prox


    def buscar(self, dato):

        actual = self._cabeza

        while actual is not None:
            if actual.dato == dato:
                return actual
            actual = actual.prox
        return None
        

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.prox

