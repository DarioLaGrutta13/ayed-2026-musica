# Declaración de uso de IA

Actualizar **en cada entrega**. Si no usaron IA, dejar una fila que lo diga. No declarar cuando sí se usó anula la entrega.

Fecha de esta versión del archivo:

| Entrega | Fecha | Herramienta (ChatGPT, Cursor, Copilot, otra) | Para qué (diseño, código, debug, docs) | Qué pegaron o generaron | Qué reescribieron / revisaron a mano | Integrante |

| --- | --- | --- | --- | --- | --- | --- |

| E1 | 3/09/26 | Gemini | Diseño de catálogo | Se le envió como ejemplo el primer diccionario de la lista y se pidió que lo recreara para todo el catálogo completo | La lista completa devuelta se utilizó para recorrer luego la información | La Grutta Dario |

| E1 | 5/09/26 | Gemini | Uso de GitHub | Se le dió como contexto lo que quería hacer sobre el repositorio | A partir de eso, se fueron haciendo preguntas para ir conociendo la herramienta y como utilizarla | La Grutta Dario |

| E2 | 16/09/26 | Gemini | código | Corrección de clase | Se le consultó para cerrar un método en una clase luego de una ciclo for o consulta lógica con if. respuesta, poner Return al final | La Grutta Dario |

| E2 | 17/09/26 | Copilot | código | Pegué mi modelo de recursión consultando por la validación que había generado --> if 0<cancion_id<len(biblio.canciones): se_encontro = False| Se reescribió la validación repasando cada id dentro del catálogo, porque ahora que estan todos los id completos funciona, pero si yo borró canciones, la cantidad seguirpa evaluando pero el órden de las canciones ya no irán acorde a los ids --> for c in catalogo: if c["id"] == cancion_id: ...| La Grutta Dario |

| E2 | 18/09/26 | Copilot | código | Ayuda con función recursiva, explicación sobre cono se relacionaba la información | La Grutta Dario |

```text
Ejemplo de explicacion:
def listar_versiones_derivadas(cancion_id, catalogo):

    listado = []

    se_encontro = False

    #Validación
    for c in catalogo:
        if c["id"] == cancion_id:
            se_encontro = True
            break

    Si no se encuentra alguna cpioncidencia entre ID y cancion:

    if not se_encontro:
        print(f"\nNo se encontró la canción con ID {cancion_id} en el catálogo.\n")
        return listado # Devuelvo caso base con listado vacío
            
    Al no ingresar por el if anterior, empieza a buscar posibles versiones
    for c in catalogo:
        if c["version_de"] == cancion_id:
            listado.append(c)
            siguiente = listar_versiones_derivadas(c["id"], catalogo)
            for sig in siguiente:
                listado.append(sig)
    return listado
```


| E2 | 19/09/26 | Copilot | docs | Pegué un error de circularidad que me estaba dando al ejecutar 'python -m src.main' | Luego de comprander el error, modifique la manera de importar funciones y clases para evitar el error. | La Grutta Dario |

| E2 | 19/09/26 | Copilot | código | Ayuda con método para borrar cancion, idea de guardar en una variable 'encontrada' como un tag de aviso | Sugerencia, guardar en una lista y reemplazar contenido | La Grutta Dario |

```text
    def eliminar_cancion_biblioteca(self, id_eliminar):

        lista_sin_cancion_borrada = []

        encontrada = False
        
        for cancion in self.canciones:
        
            if cancion['id'] == id_eliminar:
                encontrada = True
        
            else:
                lista_sin_cancion_borrada.append(cancion) 
```

| E2 | 20/09/26 | Copilot | código | Implementé el 'Try - Except' Pegué el error que me daba lo generado para entender el motivo | Reescribí la manera de utilizar 'Exception - ValueError - TypeError' | La Grutta Dario |

| E3 |  |  |  |  |  |  |
| E4 |  |  |  |  |  |  |
| E5 |  |  |  |  |  |  |
| E6 |  |  |  |  |  |  |

Compromiso: cualquiera del grupo puede explicar cualquier archivo del tag.
