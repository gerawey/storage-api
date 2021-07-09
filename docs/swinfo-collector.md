## Acerca de este proyecto
Este proyecto se trata sobre la colección de datos de todos los switches integrados en la empresa. Con la finalidad de tener un control de a donde están conectados. De tal manera que se pueda encontrar cualquier problema fácilmente.

## Modo de uso

|Metodo| Path                | Descripcion                            |
|-------------|------------------------|----------------------------- |
|POST| /switch/new          | Agregar un switch.                     |
|POST| /connect | Agregar una nueva conneccion|
|DELETE| /connect/<connecion_id>| Muestra la informacion de un solo switch.|
|GET| /switch/<switch_id>| Muestra la informacion de un solo switch.|
|GET| /switch/all      | Muestra todos los switches agregados.  |
|GET| /switch/<switch_id>/ports/all | Muestra la informacion de los puertos de un switch|
|GET| /switch/<switch_id>/ports/free | Muestra la informacion de los puertos libres de un switch|
|GET| /switch/<switch_id>/ports/busy | Muestra la informacion de los puertos ocupados de un switch|
|GET| /connect/<connecion_id>| Muestra la informacion de una connecion|



## Operaciones de consulta de datos
### Solicitar datos de un equipo de diagnóstico

- Número de Serie
- Modelo
- Puerto
- Descripcion

## Guia para articular un API JSON
La estructura del proyecto se basa en las siguientes entidades:
-	Switch (id, serial_number, model, ports, description)
- connect (id, switch_in_id, switch_out_id, port_in, port_out,description)



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
|Creacion de: modules/swinfo-collector.py y routes/swinfo-collector.py   | ba5091718ce9c46b9f6923581a7d27de2a085f37 |
