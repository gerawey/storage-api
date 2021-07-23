from json import dumps as json_dumps
import bottle

STORAGE_METHOD = environ["STORAGE_METHOD"]
if STORAGE_METHOD == 'LOCAL':
    print("Using local storage")
    from modules.storage import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
elif STORAGE_METHOD == 'GCLOUD':
    print("Using gcloud storage")
    from modules.gstorage import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
else:
    raise Exception("Storage method not set")

app = bottle.Bottle()

@app.get("/switch/new")
def get_switch(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")


@app.get("/switch/<switch_id>")
def get_movie_by_id(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")


@app.get("/switch/all")
def get_switch_all(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")


@app.get("/connect/new")
def get_connect(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

@app.get("/connect/<conexion_id>")
def get_connect_by_id(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

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
