from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    def __init__(self):
        self._elementos = ListaEnlazada()

    def apilar(self, dato):
        self._elementos.insertar_al_inicio(dato)

    def desapilar(self):

        if self.esta_vacia():
            raise PilaVaciaError("No hay acciones en el historial para deshacer.")

        tope = self.ver_tope()
        self._elementos.eliminar(tope)
        return tope


    def ver_tope(self):

        if self.esta_vacia():
            raise PilaVaciaError("No hay acciones en el historial para deshacer.")

        tope = self._elementos._cabeza.dato
        return tope


    def esta_vacia(self):
        return self._elementos.esta_vacia()

    def tamanio(self):
        return self._elementos.tamanio()

    def __iter__(self):
        return iter(self._elementos)