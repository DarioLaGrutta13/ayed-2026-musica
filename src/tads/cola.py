from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError

class Cola:

    def __init__(self):

        self._elementos = ListaEnlazada()

    def encolar(self, dato):

        self._elementos.insertar_al_final(dato)

    def desencolar(self):

        if self._elementos.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")

        frente = self.ver_frente()
        self._elementos.eliminar(frente)
        return frente

    def ver_frente(self):

        if self._elementos.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")

        frente = self._elementos._cabeza.dato
        return frente

    def esta_vacia(self):

        return self._elementos.esta_vacia()

    def tamanio(self):
        return self._elementos.tamanio()

    def __iter__(self):
        return iter(self._elementos)
