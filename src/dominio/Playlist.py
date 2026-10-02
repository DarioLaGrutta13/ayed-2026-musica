from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ItemNoEncontradoError,CancionDuplicadaError,ColeccionLlenaError,ColeccionVaciaError

class Playlist():
    def __init__(self, nombre, maximo = 10):

        # Para dar mas personalidad a la playlist, pido la opcion de un nombre
        self.nombre = nombre.title()
        self.canciones = ListaEnlazada()
        self.maximo = maximo

    def __str__(self):
        return (f"\nSu Playlist '{self.nombre}' cuenta con {self.canciones.tamanio()} canciones.")

    def agregar_cancion_playlist(self, id_agregar, biblioteca):
        
        cancion = biblioteca.buscar_cancion(id_agregar)
        
        if self.canciones.buscar(cancion) is not None:
            raise CancionDuplicadaError(f"Su canción ya se encuentra en '{self.nombre}'.")
        
        if self.canciones.tamanio() >= self.maximo:
            raise ColeccionLlenaError(f"La playlist '{self.nombre}' está llena (máximo {self.maximo}). No se puede agregar más.")

        self.canciones.insertar_al_final(cancion)
        print(f"\nCanción N°: ({cancion['id']}) '{cancion['titulo']}' de {cancion['artista']}, agregada.")

    def eliminar_cancion_playlist(self, id_eliminar):

        for cancion in self.canciones:
            if cancion['id'] == id_eliminar:
                self.canciones.eliminar(cancion)
                print(f"\nCanción N° ({id_eliminar}) - {cancion['titulo']} eliminada de la Playlist '{self.nombre}'.")
                return

        raise ItemNoEncontradoError(f"\nCanción N° {id_eliminar} no se encuentra dentro de '{self.nombre}'")

    def mostrar_canciones_playlist(self):
        
        if self.canciones.esta_vacia():
            raise ColeccionVaciaError(f"La Playlist '{self.nombre}' está vacpía..")

        for cancion in self.canciones:
            print(f"\n ({cancion['id']}) - {cancion['titulo']} - {cancion['artista']}\n")
            print("- - - - "*4)

    def conocer_duracion_total(self):

        if self.canciones.esta_vacia():
            raise ColeccionVaciaError(f"La Playlist '{self.nombre}' está vacpía..")
        
        duracion = 0
        for cancion in self.canciones:
            duracion += cancion['duracion_seg']

            duracion_minutos = round(duracion / 60) 

        print(f"\nSu Playlist '{self.nombre}', dura aproximadamente {duracion_minutos} minutos.")