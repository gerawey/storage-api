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
def store_record(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("switch", filename, json_dumps(data))
    return dict(code=501, message = "Not Implemented")


@app.get("/switch/<switch_id>")
def info_by_code(*args, code=None, **kwargs):
 payload = bottle.request.json
    print(payload)
 bottle.response.status = 501
    bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("switch", filename, json_dumps(data))
    pass
    return dict(code=501, message = "Not Implemented")

@app.get("/switch/all")
def info_by_code(*args, code=None, **kwargs):
 payload = bottle.request.json
    print(payload)
 bottle.response.status = 501
    bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("switch", filename, json_dumps(data))
    pass
    return dict(code=501, message = "Not Implemented")


@app.get("/connect/new")
def void_report(*args, **kwargs):
 payload = bottle.request.json
    print(payload)

bottle.response.status = 501
    bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("switch", filename, json_dumps(data))
    return dict(code=501, message = "Not Implemented")

@app.get("/connect/<conexion_id>")
def void_report(*args, **kwargs):
 payload = bottle.request.json
    print(payload)

bottle.response.status = 501
    bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("switch", filename, json_dumps(data))
    return dict(code=501, message = "Not Implemented")


@app.get("/switch/<switch_id>/ports/all")
def void_report(*args, **kwargs):
 payload = bottle.request.json
    print(payload)

bottle.response.status = 501
    bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("switch", filename, json_dumps(data))
    return dict(code=501, message = "Not Implemented")


@app.get("/switch/<switch_id>/ports/free")
def void_report(*args, **kwargs):
 payload = bottle.request.json
    print(payload)

bottle.response.status = 501
    bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("switch", filename, json_dumps(data))
    return dict(code=501, message = "Not Implemented")


@app.get("/switch/<switch_id>/ports/busy")
def void_report(*args, **kwargs):
 payload = bottle.request.json
    print(payload)

bottle.response.status = 501
    bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("switch", filename, json_dumps(data))
    return dict(code=501, message = "Not Implemented")
