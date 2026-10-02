class Nodo:
    def __init__(self, dato = None , prox = None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

    def __eq__(self, other):
        if type(other) != type(self):
            raise NotImplementedError('No se puede comparar un Nodo() con un ' + str(type(other)))
        elif self == other:
            return True
        return False