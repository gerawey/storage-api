## Acerca de este proyecto
Este proyecto se trata sobre la colección de datos de todos los switches integrados en la empresa. Con la finalidad de tener un control de a donde están conectados. De tal manera que se pueda encontrar cualquier problema fácilmente.

## Modo de uso

|Metodo| Path                | Descripcion                            |
|-------------|------------------------|----------------------------- |
|POST| /switch/add           | Agregar un switch.                     |
|GET| /switch-list/list      | Muestra todos los switches agregados.  |
|GET| /switch-info/switch-id | Muestra la informacion de un solo switch.|



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


--------------------------------------------------------------------------------------------
## Evaluacion - Computo en la nube
#### 1.	Crear un fork del proyecto storage-api Señalar cual es el commit-hash a partir de haber realizado el fork
| Concepto            | Commit Hash                            |
|------------------------|----------------------------- |
| Creacion de Fork          |8c9c250a11ab0ac5c2b83ceb07cc5ec8dc1560f7                    |


#### 2.	Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones. Señalar el commit-hash que contiene la creación de dichos archivos.

| Concepto            | Commit Hash                            |
|------------------------|----------------------------- |
| Creacion de docs/swinfo-collector.md         |bc7242905067ce0ecc6776a770626fe84a408d62    |
|Creacion de: modules/movie-info.py y routes/movie-info.py   | ba5091718ce9c46b9f6923581a7d27de2a085f37 |
