## Acerca de este proyecto
Este proyecto se trata sobre la colección de datos de todos los switches integrados en la empresa. Con la finalidad de tener un control de a donde están conectados. De tal manera que se pueda encontrar cualquier problema fácilmente.

## Modo de uso

Path	Descripción
/switch/add	Agregar un switch.
/switch-list/list	Muestra todos los switches agregados.
/switch-info/switch-id	Muestra la informacion del switch.
/switch-port/port/add	Agregar puerto.

## Archivos Relacionados
•	routes/switch-info.py
•	modules/switch-info.py

## Guia para articular un API JSON
La estructura del proyecto se basa en las siguientes entidades:
•	Switch (id, modelo, serial-number, puerto)



## Operaciones de Almacenamiento de datos
#### Operaciones para un switch
•	Se solicita modelo, número de serie y puerto.
•	El ID se auto asigna.
## Estructuras de solicitud y respuesta
####Registro de usuario
{
    "modelo": "Catalyst",
    "serial-number": "FGH11549"
    "puerto": "g0/0"

}

##Respuesta de registro de switch exitoso.
{ "id": "0001" }
