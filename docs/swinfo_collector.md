## Acerca de este proyecto
Este proyecto se trata sobre la colección de datos de todos los switches integrados en la empresa. Con la finalidad de tener un control de a donde están conectados. De tal manera que se pueda encontrar cualquier problema fácilmente.

## Sector
El proyecto esta enfocado al departamento de TI de cualquier tipo de empresa que utilice diferentes conexiones de switch y llevar un orden
mas eficaz de de estos.

## Modelado de datos
La estructura del proyecto se basa en las siguientes entidades:
-	Switch (id, serial_number, model, ports, description)
- connect (id, switch_in_id, switch_out_id, port_in, port_out,description)


## Rutas HTTP

|Metodo| Path                | Descripcion                            |
|-------------|------------------------|----------------------------- |
|POST| /switch/new          | Agregar un switch.                     |
|POST| /connect | Agregar una nueva conexion|
|DELETE| /switch/<switch_id>| Elimina un switch de la lista.|
|UPDATE| /switch/<switch_id>| Actualiza la informacion de un switch|
|DELETE| /connect/<conexion_id>| Elimina una conexion de la lista.|
|UPDATE| /connect/<conexion_id>| Actualiza la informacion de una conexion.|
|GET| /switch/<switch_id>| Muestra la informacion de un solo switch.|
|GET| /switch/list     | Muestra todos los switches agregados.  |
|GET| /switch/<switch_id>/ports/all | Muestra la informacion de los puertos de un switch.|
|GET| /switch/<switch_id>/ports/free | Muestra la informacion de los puertos libres de un switch.|
|GET| /switch/<switch_id>/ports/busy | Muestra la informacion de los puertos ocupados de un switch.|
|GET| /connect/<conexion_id>| Muestra la informacion de una conexion.|
|GET| /connect/list| Muestra una lista de conexiones.|


## Consulta de datos
1. Solicitar datos de un switch
- Por id
2. Solicitar datos de una conexion
- Por id
3. Solicitar todos los switches agregados
- Todos
4. Solicitar todas las conexiones
- Todos


## Operaciones de consulta de datos
### Solicitar datos de un equipo de diagnóstico

- Número de Serie
- Modelo
- Puerto
- Descripcion


## Operaciones de Almacenamiento de datos
#### Operaciones para un switch
-	Se solicita modelo, número de serie, numero de puertos y una descripcion.
-	El ID se auto asigna.

## Estructuras de switch
### Registro de switch
{

    "id": "0001",

    "serial_number": "FGH11549",  

    "model": "Catalyst",

    "ports": "24",

    "description": "Este switch esta en el IDF 4"

}

## Estructura de conexion
### Registro de connect
{

    "id": "0001",    

    "switch_in_id": "0001",

    "switch_out_id": "0002",

    "port_in": "1",

    "port_out": "1",

    "description": "Esta conexion si funciona"

}

## Respuesta de registro de switch exitoso.
{ "id": "0001" }

## Respuesta de registro de conexion exitoso.
{ "id": "0001" }

## Ejemplos de interacciones con el servidor

`POST /switch
Recibe una estructura de registro de un nuevo switch.
201, registrar un switches regresa estructura de id para el nuevo switch.
D.O.M, regresa mensaje de fallo.`

`GET /switch/list
200, regresa una lista de todos los switches agregados.
D.O.M, regresa mensaje de fallo en formato json.
curl http://localhost:8080/swinfo-collector/json-X GET -H "Content-Type: application/json" --data '{​​​​​​​"switch_id": "All"}​​​​​​​'`

`GET /switch/<switch_id>
200, regresa datos de un switch con id.
D.O.M, regresa mensaje de fallo en formato json.
curl http://localhost:8080/swinfo-collector/<switch_id> -X GET -H "Content-Type: application/json" --data '{​​​​​​​"switch_id": "0001"}`

`POST /switch/<switch_id>
201, actualizar informacion de un switch.
D.O.M, regresa mensaje de fallo.`

`POST /connect/<conexion_id>
201, agregar una nueva conexion.
D.O.M, regresa mensaje de fallo.`

`GET /connect/all
200, regresa una lista de todos las conexiones agregadas.
D.O.M, regresa mensaje de fallo en formato json.
curl http://localhost:8080/swinfo-collector/<conexion_id> GET -H "Content-Type: application/json" --data '{​​​​​​​"conexion_id": "All"}​​​​​​​'`

`GET /switch/<switch_id>/ports/free
200, regresa una lista de todos los puertos libres de un switch.
D.O.M, regresa mensaje de fallo en formato json.
curl http://localhost:8080/swinfo-collector//<switch_id>/ports/free GET -H "Content-Type: application/json" --data '{​​​​​​​"switch_id": "All"}​​​​​​​'`



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

#### 3. Creacion de las rutas.
| Concepto            | Commit Hash                            |
|------------------------|----------------------------- |
|Creacion de: routes/swinfo-collector.py   | ba5091718ce9c46b9f6923581a7d27de2a085f37 |

#### 4. Creacion de documento de funciones.
| Concepto            | Commit Hash                            |
|------------------------|----------------------------- |
|Creacion de: modules/swinfo-collector.py   | ba5091718ce9c46b9f6923581a7d27de2a085f37 |

#### 5. Creacion de mock ups.

| Concepto            | Commit Hash                            |
|------------------------|----------------------------- |
|Creacion de:   |  |
