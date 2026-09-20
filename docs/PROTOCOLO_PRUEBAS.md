# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | No Corrido  |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |  |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa | No Corrido |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) | No Corrido |  |
| P05 | E2 | Buscar en Biblioteca un ID inexistente | id = 80 | Mensaje de aviso, programa continua | No Corrido | --- |
| P06 | E2 | Buscar en Playlist un ID inexistente | id = -70 | Mensaje de aviso, programa continua | No Corrido | --- |
| P07 | E2 | Buscar una canción que no existe para ver su detalle | id = 514 | Mensaje de aviso, programa continua | No Corrido | --- |
| P08 | E2 | Buscar en Biblioteca un ID pasando caracteres | id = uno | Mensaje de aviso, programa continua | No Corrido | --- |
| P09 | E2 | Agregar a Playlist un ID inexistente | id = 789 | Mensaje de aviso, programa continua | No Corrido | --- |
| P10 | E2 | Eliminar de Playlist un ID inexistente | id =  71 | Mensaje de aviso, programa continua | No Corrido | --- |
| P11 | E2 | Listar Playlist sin canciones dentro | Opción = 7 | Notificacion de Playlist vacía | No Corrido | --- |
| P12 | E2 | Eliminar de Playlist un ID inexistente | id =  71 | Mensaje de aviso, programa continua | No Corrido | --- |
| P13 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia |  |  |
| P14 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue |  |  |
| P15 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue |  |  |
| P16 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones |  |  |
| P17 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P18 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P19 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P20 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P21 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P22 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P23 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |