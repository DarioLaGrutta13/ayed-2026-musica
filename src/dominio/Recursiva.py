
def versiones_de(id_buscar, biblio ,versiones):

    canciones_con_versiones = biblio.versiones_directas(id_buscar, versiones)

    if not canciones_con_versiones:
        return [id_buscar]

    resultado = [id_buscar]

    for version in canciones_con_versiones:
        resultado += versiones_de(version,biblio, versiones)

    return resultado


