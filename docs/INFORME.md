# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical 
- Decidimos trabajar este tema dentro del grupo porque la música es algo que nos interpela a todos. Ya sea por cuestiones de gustos diarios de escuchar música, o simplemente de a ratos por videos, radio o streaming, la música esta presente. Además, consideramos que siempre es mejor poder trabajar con datos e información con la que se tiene más afinidad y alcance, con el objetivo de poder comprender mejor lo solicitado y trabajado.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Dentro de nuestra elección definiriamos como ítem principal a la Canción ("título"), ya que la búsqueda y reconocimiento principal del usuario es mediante ese dato. Por otro lado, adentrandonos dentro de lo que sería mutable o no, tenemos dos visiones:
    1) Dentro del aspecto técnico, trabajaremos con los contenedores de tipo lista y diccionario, donde ambos son de caracter mutable como bien vimos y sus valores se pueden sobreescribir y/o borrar.

    2) Tomando una mirada lógica del modelo, aquello inmutable será la información raíz y principal. Por ejemplo, el nombre de una canción, su lanzamiento (álbum y año de lanzamiento), id. Por otro lado, adentrandonos en las posibilidades, dentro de una canción pueden aparecer métricas extra como cantidad de reproducciones, likes, las cuáles son de índole variable/mutable; o hasta implementaciones que indiquen nuevas versiones y modifiquen el género, la duración, etc. Sin embargo, un detalle no menor a tener en cuenta, esta nueva versión formaría una nueva entidad y no reemplazaría a la original.

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

- Función: versiones_de() ubicada en src/dominio/Recursiva.py
Internamente la función mencionada hace uso del método "versiones_directas()". Esta se encuentra definida en la clase 'Biblioteca' y recibe como argumentos a un id_buscar, un objeto de tipo 'Biblioteca' y la información de las versiones.

- Caso base: Devolver la lista vacía.
En caso de que 'Biblioteca.versiones_directas()' devuelva una lista vacía, directamente se analiza esa situación. En caso de ser verdadero el supuesto, se finaliza el análisis y notifica que no hay versiones posteriores.

- Caso recursivo: Nuevo llamado a versiones_de()
Luego de pasar el caso base, se determina que el contenido devuelto por el métido versiones_directas(), sea el próximo caso a analizar. de esa manera, para poder analizar ese caso se utiliza el caso recursivo de volver a utilizar versiones_de().

- Traza de un ejemplo real del dataset:

A)Llamamos la funcion y proporcionamos los parámetros correspondientes 
    versiones_de(id_buscar, versiones)
    Ej: versiones_de(19, mi_biblioteca ,versiones) 
    --> Siendo mi_biblioteca la lista con todas nuestras canciones
    --> Siendo versiones nuestra lista que guarda el registro de versiones

B)Internamente, llamamos al método mi_biblioteca.versiones_directas(19, versiones). Este método lo que hace es, gracias al id_buscar proporcionado (19), encontrar posteriores versiones para dicho título. En caso de econtrar algún registro que coincida, lo guarda en una lista que luego devuelve. 
    Ej: siendo 19 el 'id' a buscar, devuelve una coincidencia con el 'id' 63 porque es 'version_de' : 19

C) Teniendo como registro hasta ahora que 19 --> 63 --> ¿63 tiene una version posterior?
En este paso es que se aplica nuevamente la búsqueda aplicando el metodo recursivo con version_de()

D) Finalmente para este caso, nos encontramos con que el recorrido final es 19-->63 y allí termina porque no hay otro título posterior a ese.

```text
Función: versiones_de(19, mi_biblioteca ,versiones)
Caso base: Si la canción no tiene una versión posterior → devolver [id] - [titulo] de la canción buscada.
Caso recursivo: [id] + versiones_de(id_buscar , biblioteca , versiones)
Traza para 'Flaca' (id 19): según versiones.csv, 19-->63.

Llamada 1: versiones_directas(19, versiones) --> tiene siguiente (63)
→ devuelve [19] + versiones_directas(63, versiones)

Llamada 2: versiones_directas(63, versiones) --> no tiene siguiente versión
entonces, versiones_directas(63, versiones) --> NO tiene siguiente (caso base)

→ devuelve [63]

Resultado: [19] + [63] = [19, 63]
```

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
