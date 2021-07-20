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
>>>>>>> ca8357a (Se crearon rutas especificas)
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501,{"code" :"501", "messaje" : "Not implement"})

@app.get("/switch/<switch_id>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented")

@app.get("/switch/all")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented")

@app.get("/connect/new")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented")

@app.get("/connect/<conexion_id>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented")

@app.get("/switch/<switch_id>/ports/all")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented")

@app.get("/switch/<switch_id>/ports/free")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented")

@app.get("/switch/<switch_id>/ports/busy")
    def store_record(*args, **kwargs):
        #aqui codigo
        return dict(code=501, message="not implemented")
