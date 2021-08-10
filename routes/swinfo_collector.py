import bottle
from modules.bottles import BottleJson
from modules.swinfo_collector import (
    add_switch,
    add_connect,
    get_switch_all,
    update_switch,
    get_connect_all
)

app = BottleJson()

@app.post("/switch")
def switch(*args, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
    try:
        #switch_id: int(payload['switch_id'])
        serial_number = str(payload['Serial number'])
        model = str(payload['Model'])
        ports = str(payload['ports'])
        description = str(payload['description'])
        id = str(payload['id'])
        respuesta = add_switch(**payload)
        raise bottle.HTTPError(201, "Switch Agregado")
    except:
        raise bottle.HTTPError(400, "Error no se pudo agregar switch")
    raise bottle.HTTPError(500,"Error general")


@app.get("/switch/<switch_id>")
def switch_by_id(*args, **kwargs):
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


@app.get("/switch/all")
def get_switch_all(*args, **kwargs):
    try:
       respuesta = get_switch_all()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


@app.get("/connect/new")
def add_connect(*args, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
    try:
        #switch_id: int(payload['switch_id'])
        switch_in_id = str(payload['switch in id'])
        switch_out_id = str(payload['switch out id'])
        port_in = str(payload['port in'])
        port_out = str(payload['port out'])
        id = str(payload['id'])
        respuesta = creador_nota(**payload)
        raise bottle.HTTPError(201, "Conexion Agregada")
    except:
        raise bottle.HTTPError(400, "Error no se pudo agregar conexion")
    raise bottle.HTTPError(500,"Error general")

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
