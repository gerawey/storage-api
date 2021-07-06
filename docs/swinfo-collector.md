## Acerca de este proyecto
Este proyecto se trata sobre la colección de datos de todos los switches integrados en la empresa. Con la finalidad de tener un control de a donde están conectados. De tal manera que se pueda encontrar cualquier problema fácilmente.

## Modo de uso

|Metodo| Path                   | Descripcion                           |
|    |------------------------|---------------------------------------|
|POST| /switch/add            | Agregar un switch.                    |
|GET| /switch-list/list      | Muestra todos los switches agregados. |
|GET| /switch-info/switch-id | Muestra la informacion de un solo switch.    |



## Operaciones de consulta de datos
### Solicitar datos de un equipo de diagnóstico

- Modelo
- Número de Serie
- Puerto

## Guia para articular un API JSON
La estructura del proyecto se basa en las siguientes entidades:
-	Switch (id, modelo, serial-number, puerto)
- conexion (id, switch1, serial-number1, puerto1, switch2,serial-number2, puerto2)



## Operaciones de Almacenamiento de datos
#### Operaciones para un switch
-	Se solicita modelo, número de serie y puerto.
-	El ID se auto asigna.

## Estructuras de switch
### Registro de switch
{

    "modelo": "Catalyst",

    "serial-number": "FGH11549",

    "puerto": "g0/0"


}
## Estructura de conexion
### Registro de conexion
{

  "modelo": "Catalyst 2960 24-S",

  "serial-number": "FGH11549",

  "puerto": "g0/0",

  "modelo": "Catalyst 2960 24TC-L:",

  "serial-number": "FGH1222",

  "puerto": "g0/1"


}

## Respuesta de registro de switch exitoso.
{ "id": "0001" }

## Respuesta de registro de conexion exitoso.
{ "id": "0001" }
