# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical 
- Decidimos trabajar este tema dentro del grupo porque la música es algo que nos interpela a todos. Ya sea por cuestiones de gustos diarios de escuchar música, o simplemente de a ratos por videos, radio o streaming, la música esta presente. Además, consideramos que siempre es mejor poder trabajar con datos e información con la que se tiene más afinidad y alcance, con el objetivo de poder comprender mejor lo solicitado y trabajado.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Dentro de nuestra elección definiriamos como ítem principal a la Canción ("título"), ya que la búsqueda y reconocimiento principal del usuario es mediante ese dato. Por otro lado, adentrandonos dentro de lo que sería mutable o no, tenemos dos visiones:
    1) Dentro del aspecto técnico, trabajaremos con los contenedores de tipo lista y diccionario, donde ambos son de caracter mutable como bien vimos y sus valores se pueden sobreescribir y/o borrar.
    2) Tomando una mirada lógica del modelo, aquello inmutable será la información raíz y principal. Por ejemplo, el nombre de una canción, su lanzamiento (álbum y año de lanzamiento), id. Por otro lado, adentrandonos en las posibilidades,
dentro de una canción pueden aparecer métricas extra como cantidad de reproducciones, likes, las cuáles son de índole variable/mutable; o hasta implementaciones que indiquen nuevas versiones y modifiquen el género, la duración, etc.
Sin embargo, un detalle no menor a tener en cuenta, esta nueva versión formaría una nueva entidad y no reemplazaría a la original.

Por último el catálogo será nuestra base principal. Consecuentemente, podremos obtener o armar una colección principal que funcionaría como playlist. Dicha colección, estará integrada por nuestras canciones dentro del catálogo. 
Posteriormente, para cada canción obtendremos un historial de reproducción, que sería lo denominado pila y por último la cola de reproducción que indicaría la sucesión de canciones a escuchar.

```text
                                       Catálogo de canciones
                                                 │
                                                 ▼
                                       Colección principal
                                                 │
                                              ┌──┴──┐
                                          ▼            ▼
                                        Pila          Cola
                                     (historial) (pendientes)
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
