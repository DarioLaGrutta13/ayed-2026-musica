from src.config import TEMA
from src.dominio.canciones import bienvenida, eleccion_opciones

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():

    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")

    print(f"\n=== {nombre}=== AyED C2 2026 ===\n")
    print("1) Listar catálogo.\n")
    print("2) Buscar canción y ver detalle.\n")
    print("3) Salir.\n")

    eleccion_opciones()

    # print("4. Ordenar")
    # print("5. Operación recursiva")
    # print("6. Colección principal (equipo / menú / playlist)")
    # print("7. Historial (pila)")
    # print("8. Cola")
    # print("9. Guardar / cargar archivos")
    # print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

bienvenida()
mostrar_menu()
