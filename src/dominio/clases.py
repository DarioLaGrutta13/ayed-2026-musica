class Cancion():
    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg

    def __str__(self):
        return f"\n({self.id}) - {self.titulo} - {self.artista}"

class Biblioteca():
    def __init__(self,lista_canciones):

        #creamos la lista cons todas nurestras canciones disponibles
        self.canciones = lista_canciones
        
    def __str__(self):
        return(F"\nLa Biblioteca Musical cuenta con {len(self.canciones)} canciones. Su duración aproximada es de: {self.minutos_totales()} minutos.")

    def minutos_totales(self):
            duracion = 0
            for cancion in self.canciones:
                duracion += cancion['duracion_seg']
    
            duracion_minutos = round(duracion / 60)
    
            return duracion_minutos

    def eliminar_cancion_biblioteca(self, id_eliminar):

        lista_sin_cancion_borrada = []

        encontrada = False
        
        for cancion in self.canciones:
        
            if cancion['id'] == id_eliminar:
                encontrada = True
        
            else:
                lista_sin_cancion_borrada.append(cancion)

        if encontrada:
            self.canciones = lista_sin_cancion_borrada 
            print(f"\nCanción N°: {id_eliminar} eliminada de su Biblioteca.")
            
        else:
            print(f"\nCanción N°: {id_eliminar} no encontrada en su Biblioteca.")
            
    def mostrar_canciones_biblioteca(self):

        if len(self.canciones) == 0:
            print("\nLa bilioteca musical está vacía..")
        else:
            for cancion in self.canciones:
                
                print(
                    f"\n ({cancion['id']}) - {cancion['titulo']} - {cancion['artista']}")
                print(" - - - "*7)


    def versiones_directas(self, id_buscar, versiones):
        directas = []


        for version in versiones:

            if version["version_de"] == id_buscar:

                directas.append(version["cancion_id"])

        return directas
    
class Playlist():
    def __init__(self, nombre):

        # Para dar mas personalidad a la playlist, pido la opcion de un nombre
        self.nombre = nombre.title()
        self.canciones = []

    def __str__(self):
        return (f"\nSu Playlist '{self.nombre}' cuenta con {len(self.canciones)} canciones.")

    def agregar_cancion_playlist(self, id_agregar, biblioteca):

        for cancion in self.canciones:

            if cancion['id'] == id_agregar:
                print(f"\nSu canción ya se encuentra en '{self.nombre}'.")
                return

        for cancion in biblioteca.canciones:

            if cancion['id'] == id_agregar:
                
                self.canciones.append(cancion)
                print(f"\nCanción N°: ({cancion['id']}) '{cancion['titulo']}' de {cancion['artista']}, agregada.")

                return
  
        print(f"\nEl ID ({id_agregar}) no se encontró en nuestra biblioteca.")

    def eliminar_cancion_playlist(self, id_eliminar):

        playlist_sin_cancion_borrada = []

        encontrada = False

        for cancion in self.canciones:

            if cancion['id'] == id_eliminar:
                encontrada = True

            else:
                playlist_sin_cancion_borrada.append(cancion)
        if encontrada:
            self.canciones = playlist_sin_cancion_borrada 
            print(f"\nCanción N°: {id_eliminar} eliminada de su Playlist '{self.nombre}'.")

        else:
            print(f"\nCanción N°: {id_eliminar} no encontrada en '{self.nombre}'.")

    def mostrar_canciones_playlist(self):
        if len(self.canciones) == 0:
            print("\nSu bilioteca musical está vacía..")
        else:
            for cancion in self.canciones:
                print(
                    f"\n ({cancion['id']}) - {cancion['titulo']} - {cancion['artista']}\n")
                print("- - - - "*4)

    def conocer_duracion_total(self):

        cantidad_canciones = len(self.canciones)
        if cantidad_canciones:

            duracion = 0
            for cancion in self.canciones:
                duracion += cancion['duracion_seg']

            duracion_minutos = round(duracion / 60) 

            print(
                f"\nSu Playlist '{self.nombre}', dura aproximadamente {duracion_minutos} minutos.")