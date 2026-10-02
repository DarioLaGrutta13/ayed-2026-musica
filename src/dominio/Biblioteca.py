from src.excepciones import ItemNoEncontradoError

class Biblioteca():
    def __init__(self,lista_canciones):

        #creamos la lista cons todas nurestras canciones disponibles
        self._canciones = lista_canciones
        
    def __str__(self):
        return(F"\nLa Biblioteca Musical cuenta con {len(self._canciones)} canciones. Su duración aproximada es de: {self.minutos_totales()} minutos.")

    def cantidad_canciones(self):
        return len(self._canciones)

    def buscar_cancion(self, id_buscar):

        for cancion in self._canciones:
            if cancion['id'] == id_buscar:
                return cancion

        raise ItemNoEncontradoError(f"El ID ({id_buscar}) no se encontró en nuestra Biblioteca.")

    
    def minutos_totales(self):
            
            duracion = 0
            for cancion in self._canciones:
                duracion += cancion['duracion_seg']
    
            duracion_minutos = round(duracion / 60)
    
            return duracion_minutos

    def eliminar_cancion_biblioteca(self, id_eliminar):

        lista_sin_cancion_borrada = []

        encontrada = False
        
        for cancion in self._canciones:
        
            if cancion['id'] == id_eliminar:
                encontrada = True
        
            else:
                lista_sin_cancion_borrada.append(cancion)

        if encontrada:
            self._canciones = lista_sin_cancion_borrada 
            print(f"\nCanción N°: {id_eliminar} eliminada de su Biblioteca.")
            
        else:
            print(f"\nCanción N°: {id_eliminar} no encontrada en su Biblioteca.")
            
    def mostrar_canciones_biblioteca(self):

        if self.cantidad_canciones() == 0:
            print("\nLa bilioteca musical está vacía..")
        else:
            for cancion in self._canciones:
                
                print(
                    f"\n ({cancion['id']}) - {cancion['titulo']} - {cancion['artista']}")
                print(" - - - "*7)


    def versiones_directas(self, id_buscar, versiones):
        directas = []

        for version in versiones:

            if version["version_de"] == id_buscar:

                directas.append(version["cancion_id"])

        return directas
    