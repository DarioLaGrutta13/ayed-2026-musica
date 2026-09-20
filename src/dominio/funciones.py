from src.dominio.Recursiva import versiones_de
from src.dominio.canciones import biblio, mi_primer_playlist, versiones
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
    print("0) Salir.\n")


def mostrar_detalles():

    num_cancion = pedir_opcion(f"\nDentro de nuestras {len(biblio.canciones)} canciones, ingrese el número de la canción que le gustaría ver: ")

    if num_cancion < 1 or num_cancion > len(biblio.canciones):
        print("\nOpción inválida, su elección no es correcta. Por favor, verifique su ingreso.\n")
    else:
        print("\nLa información que poseemos de su canción elegida es: \n")
        print(f"Título: {biblio.canciones[num_cancion-1]['titulo']}")
        print(f"Artista: {biblio.canciones[num_cancion-1]['artista']}")
        print(f"Álbum: {biblio.canciones[num_cancion-1]['album']}")
        print(f"Género: {biblio.canciones[num_cancion-1]['genero']}")
        print(f"Año: {biblio.canciones[num_cancion-1]['anio']}")
        print(
            f"Duración (segundos): {biblio.canciones[num_cancion-1]['duracion_seg']}")


def buscar_versiones():
    try:
        id_buscar = pedir_opcion("\nIngrese el ID una canción para buscar otras versiones: ")

        existe = False
        
        for c in biblio.canciones:
        
            if c["id"] == id_buscar:
        
                existe = True

                break

    except TypeError:
            print("\nError: Ingrese un número de ID válido.")

    if not existe:
        print(f"\nEl ID {id_buscar} no fue encontrado..")

    else:
        otras_versiones = versiones_de(id_buscar, biblio ,versiones)
            
        if len(otras_versiones) == 1:
            print(
                    f"\nNo se encontraron otras versiones para la canción: ({biblio.canciones[id_buscar-1]['id']}) - '{biblio.canciones[id_buscar-1]['titulo']}' de {biblio.canciones[id_buscar-1]['artista']}.")
        else:
            print(f"\nHay '{len(otras_versiones)}' versiones de la canción: '{biblio.canciones[id_buscar-1]['titulo']}'.\n")
            for version in otras_versiones:
                print(f"\nID: {biblio.canciones[version-1]['id']}, Título: {biblio.canciones[version-1]['titulo']}, Artista: {biblio.canciones[version-1]['artista']}, Álbum: {biblio.canciones[version-1]['album']}, Año: {biblio.canciones[version-1]['anio']}, Duración (segundos): {biblio.canciones[version-1]['duracion_seg']}")
    

def ejecutar():

    bienvenida()

    while True:

        mostrar_menu()

        eleccion = pedir_opcion("\nIngrese la opción deseada: ")

        if eleccion < 0 or eleccion > 8:
            print("- - - - - "*4)
            print("\nOpción inválida. Por favor, ingrese un número entre 0 y 8.\n")
            print("- - - - - "*4)
            continue

        if eleccion == 0:
            print(" ")
            print("- - - - - "*6)
            print("\nMuchas gracias por ver nuestro catálogo musical. Nos vemos!\n")
            print("- - - - - "*6)
            break
        elif eleccion == 1:
            print("Las canciones que posee nuestra biblioteca son: \n")
            biblio.mostrar_canciones_biblioteca()

        elif eleccion == 2:
            mostrar_detalles()

        elif eleccion == 3:
            buscar_versiones()

        elif eleccion == 4:
            id_borrar = int(input("\nIngrese el numero de cancion que quiere eliminar: "))
            biblio.eliminar_cancion_biblioteca(id_borrar)

        elif eleccion == 5:
            id_agregar = pedir_opcion(f"\nIngrese el numero de cancion que quiere agregar. Recuerde que contamos con {len(biblio.canciones)} canciones: ")

            mi_primer_playlist.agregar_cancion_playlist(id_agregar, biblio)

        elif eleccion == 6:

            id_eliminar = pedir_opcion("\nIngrese el numero de cancion que quiere eliminar: ")
            mi_primer_playlist.eliminar_cancion_playlist(id_eliminar)

        elif eleccion == 7:
            mi_primer_playlist.mostrar_canciones_playlist()

        elif eleccion == 8:
            mi_primer_playlist.conocer_duracion_total()

        

        # print("4. Ordenar")

        # print("6. Colección principal (equipo / menú / playlist)")
        # print("7. Historial (pila)")
        # print("8. Cola")
        # print("9. Guardar / cargar archivos")
        # print("0. Salir")