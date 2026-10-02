from src.dominio.Recursiva import versiones_de
from src.dominio.canciones import biblio, mi_primer_playlist, versiones
from src.dominio.cola_reproduccion import cola_reproduccion
from src.dominio.historial import historial
from src.excepciones import ItemNoEncontradoError, CancionDuplicadaError,ColeccionLlenaError,ColeccionVaciaError,PilaVaciaError,ColaVaciaError
from src.config import TEMA


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca Musical", }


def pedir_opcion(pedido):

    while True:

        try:
            eleccion = int(input(pedido))
            return eleccion

        except ValueError:
            print("- - - - - "*4)
            print("\nPor favor, ingrese un número válido.\n")
            print("- - - - - "*4)
            continue


def bienvenida():

    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")

    print(f"\n=== Bienvenido a: {nombre} === AyED C2 2026 ===\n")

    print(biblio)
    print(mi_primer_playlist)

    print("\nA continuación, le brindaremos las opciones del menú disponibles: \n")
    return


def mostrar_menu():

    print("\n1) Listar Biblioteca.\n")
    print("2) Buscar canción y ver detalle.\n")
    print("3) Enumerar versiones de canciones.\n")
    print("4) Eliminar cancion de la Biblioteca\n")
    print(f"5) Agregar cancion a la Playlist: '{mi_primer_playlist.nombre}'\n")
    print(
        f"6) Eliminar cancion de la playlist: '{mi_primer_playlist.nombre}'\n")
    print(f"7) Listar playlist: '{mi_primer_playlist.nombre}'\n")
    print(
        f"8) Conocer la duración total de playlist: '{mi_primer_playlist.nombre}'\n")
    print("9) Agregar cancion a la cola de reproducción.\n")
    print("10) Reproducir la siguiente cancion de la cola.\n")
    print("11) Ver la cola de reproducción.\n")
    print("12) Ver el historial de reproducción.\n")
    print("13) Deshacer (sacar la última del historial).\n")
    print("0) Salir.\n")


    # print("4. Ordenar")
    # print("9. Guardar / cargar archivos")
    # print("0. Salir")


def mostrar_detalles():

    num_cancion = pedir_opcion(
        f"\nDentro de nuestras {biblio.cantidad_canciones()} canciones, ingrese el número de la canción que le gustaría ver: ")

    cancion = biblio.buscar_cancion(num_cancion)

    print("\nLa información que poseemos de su canción elegida es: \n")
    print(f"Título: {cancion['titulo']}")
    print(f"Artista: {cancion['artista']}")
    print(f"Álbum: {cancion['album']}")
    print(f"Género: {cancion['genero']}")
    print(f"Año: {cancion['anio']}")
    print(f"Duración (segundos): {cancion['duracion_seg']}")


def buscar_versiones():
    
    id_buscar = pedir_opcion("\nIngrese el ID una canción para buscar otras versiones: ")

    cancion = biblio.buscar_cancion(id_buscar)

    otras_versiones = versiones_de(id_buscar, biblio, versiones)

    if len(otras_versiones) == 1:
        print(f"\nNo se encontraron otras versiones para la canción: ({cancion['id']}) - '{cancion['titulo']}' de {cancion['artista']}.")
    else:
        print(f"\nHay '{len(otras_versiones)}' versiones de la canción: '{cancion['titulo']}'.\n")
        for version in otras_versiones:
            cancion_version = biblio.buscar_cancion(version)
            print(f"\nID: {cancion_version['id']}, Título: {cancion_version['titulo']}, Artista: {cancion_version['artista']}, Álbum: {cancion_version['album']}, Año: {cancion_version['anio']}, Duración (segundos): {cancion_version['duracion_seg']}")


def agregar_a_cola():
    id_agregar = pedir_opcion("\nIngrese el ID de la canción que quiere agregar a la cola de reproducción: ")

    cancion = biblio.buscar_cancion(id_agregar)

    cola_reproduccion.encolar(cancion)
    print(f"\n'{cancion['titulo']}' de {cancion['artista']} se agregó a la cola de reproducción.")


def reproducir_siguiente():
    cancion = cola_reproduccion.desencolar()

    historial.apilar(cancion)
    print(f"\nReproduciendo: ({cancion['id']}) '{cancion['titulo']}' de {cancion['artista']}... 💃🕺")


def mostrar_cola():
    if cola_reproduccion.esta_vacia():
        print("\nLa cola de reproducción está vacía..")
    else:
        print("\nPróximas canciones (la primera es la que suena a continuación): ")
        for cancion in cola_reproduccion:
            print(f"\n ({cancion['id']}) - {cancion['titulo']} - {cancion['artista']}")

def mostrar_historial():
    if historial.esta_vacia():
        print("\nEl historial de reproducción está vacío..")
    else:
        print("\nHistorial (la primera es la última que se reprodujo): ")
        for cancion in historial:
            print(f"\n ({cancion['id']}) - {cancion['titulo']} - {cancion['artista']}")

def deshacer_historial():
    cancion = historial.desapilar()
    print(f"\n'{cancion['titulo']}' de {cancion['artista']} se quitó del historial.")

def ejecutar():

    bienvenida()

    while True:

        mostrar_menu()

        eleccion = pedir_opcion("\nIngrese la opción deseada: ")

        if eleccion < 0 or eleccion > 13:
            print("- - - - - "*4)
            print("\nOpción inválida. Por favor, ingrese un número entre 0 y 13.\n")
            print("- - - - - "*4)
            continue

        if eleccion == 0:
            print(" ")
            print("- - - - - "*6)
            print("\nMuchas gracias por ver nuestro catálogo musical. Nos vemos!\n")
            print("- - - - - "*6)
            break

        try: 
            if eleccion == 1:
                print("Las canciones que posee nuestra biblioteca son: \n")
                biblio.mostrar_canciones_biblioteca()

            elif eleccion == 2:
                mostrar_detalles()

            elif eleccion == 3:
                buscar_versiones()

            elif eleccion == 4:
                id_borrar = pedir_opcion("\nIngrese el numero de cancion que quiere eliminar: ")
                biblio.eliminar_cancion_biblioteca(id_borrar)

            elif eleccion == 5:
                id_agregar = pedir_opcion(f"\nIngrese el numero de cancion que quiere agregar. Recuerde que contamos con {biblio.cantidad_canciones()} canciones: ")
                mi_primer_playlist.agregar_cancion_playlist(id_agregar, biblio)

            elif eleccion == 6:
                id_eliminar = pedir_opcion("\nIngrese el numero de cancion que quiere eliminar: ")
                mi_primer_playlist.eliminar_cancion_playlist(id_eliminar)

            elif eleccion == 7:
                mi_primer_playlist.mostrar_canciones_playlist()

            elif eleccion == 8:
                mi_primer_playlist.conocer_duracion_total()

            
            elif eleccion == 9:
                agregar_a_cola()

            elif eleccion == 10:
                reproducir_siguiente()

            elif eleccion == 11:
                mostrar_cola()

            elif eleccion == 12:
                mostrar_historial()

            elif eleccion == 13:
                deshacer_historial()

        except ItemNoEncontradoError as error:
            print(f"\n{error}")

        except CancionDuplicadaError as error:
            print(f"\n{error}")

        except ColeccionLlenaError as error:
            print(f"\n{error}")

        except ColeccionVaciaError as error:
            print(f"\n{error}")

        except ColaVaciaError as error:
            print(f"\nNo hay canciones para reproducir. {error}")

        except PilaVaciaError as error:
            print(f"\nNo hay canciones en el historial. {error}")
