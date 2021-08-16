import bottle
from bottle import route, run, post, request
from modules.bottles import BottleJson
from modules.swinfo_collector import (
    add_switch,
    add_connect,
    get_switch_all,
    update_switch,
    get_connect_all
)

app = BottleJson()

@app.get("/")
    #Default route


 # curl http://localhost:8080/switch/addswitch -X POST  -H 'Content-Type: application/json' -d '{"switch_id": "001","serial_number": "FGH11549", "model": "Catalyst", "ports": "24", "description": "Esta en el IDF 3"}'
 # curl http://localhost:8080/switch/addswitch -X POST  -H 'Content-Type: application/json' -d '{"switch_id": "002","serial_number": "FGH11549", "model": "Catalyst", "ports": "24", "description": "Esta en el IDF 2"}'

@app.post("/addswitch")
def addswitch(*args, **kwargs):
    payload = bottle.request.json
    try:
        str(payload.get('serial_number'))
        str(payload.get('model'))
        str(payload.get('ports'))
        str(payload.get('description'))
        str(payload.get('switch_id'))
        add_switch(**payload)
        bottle.response.body="Switch Agregado"
        bottle.response.status=201
        bottle.response.headers['Content-type']="text"
        return
    except:
        raise bottle.HTTPError(400, "Error no se pudo agregar switch")

# curl http://localhost:8080/connect/addconnect -X POST -H 'Content-Type: application/json' -d '{"connect_id": "001", "switch_in_id": "0001", "switch_out_id": "002", "port_in": "24", "port_out": "24"}'
@app.post("/addconnect")
def addconnect(*args, **kwargs):
    payload = bottle.request.json
    try:
        str(payload.get('connect_id'))
        str(payload.get('switch_in_id'))
        str(payload.get('switch_out_id'))
        str(payload.get('port_in'))
        str(payload.get('port_out'))
        respuesta = add_connect(
            connect_id=payload.get('connect_id'),
            switch_in_id=payload.get('switch_in_id'),
            switch_out_id=payload.get('switch_out_id'),
            port_in=payload.get('port_in'),
            port_out=payload.get('port_out')
        )
        bottle.response.body="Connect Agregado"
        bottle.response.status=201
        bottle.response.headers['Content-type']="text"
        return
    except:
        raise bottle.HTTPError(400, "Error no se pudo agregar la conexion")

@app.get("/<id>")
def query_n_s(*args, id=None, **kwargs):
    try:
        respuesta = query_s(id = id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)

@app.post("/switch/<switch_id>")
def updateswitch(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        switch_id = str(payload['switch_id'])
        serial_number = str(payload['serial_number'])
        model = str(payload['model'])
        ports = str(payload['ports'])
        description = str(payload['description'])
        print("Datos validos")
        respuesta = update_switch(**payload)
        print(respuesta)
        print("Almost done")
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, "Movie data has been updated")

# curl http://localhost:8080/switch/list -X GET
@app.get("/switch/list")
def get_switchs(*args, **kwargs):
    try:
       respuesta = get_switch_all()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)



@app.get("/connect/<conexion_id>")
def get_connect_by_id(*args, **kwargs):
        payload = bottle.request.json
        print(payload)
        try:
            id = str(payload['id'])
            print("ID valida")
            respuesta = query_information(**payload)
            raise bottle.HTTPError(201)
        except:
            raise bottle.HTTPError(501, "ID invalida")
        raise bottle.HTTPError(500, "Error general")

@app.get("/switch/<switch_id>/ports/all")
def get_switch_all_ports(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")


@app.get("/switch/<switch_id>/ports/free")
def get_switch_free_ports(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")


@app.get("/switch/<switch_id>/ports/busy")
def get_switch_busy_ports(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")
