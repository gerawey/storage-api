from os import environ
from json import dumps as json_dumps
import bottle
from modules.cors import enable_cors
import modules.utils as utils

STORAGE_METHOD = environ["STORAGE_METHOD"]
if STORAGE_METHOD == 'LOCAL':
    print("Using local storage")
    from modules.storage import store_bytes, store_string, query_storage
elif STORAGE_METHOD == 'GCLOUD':
    print("Using gcloud storage")
    from modules.gstorage import store_bytes, store_string
else:
    raise Exception("Storage method not set")

app = bottle.Bottle()


@app.route("/file", method=["POST", "OPTIONS"])
@enable_cors
def route_file(*args, **kwargs):
    """
    This function provides a way to store a single file.
    It recieves a regular html form with a single field named
    `file`.
    """
    file = bottle.request.files.get("file")
    store_bytes("files", file.filename, file.file.read())
    bottle.response.status = 201
    bottle.response.content_type = "application/json"
    return dict(store="success")


@app.route("/json", method=["POST", "OPTIONS"])
@enable_cors
def route_json(*args, **kwargs):
    payload = bottle.request.json
    now_str = utils.get_timestamp()
    _hash = f"{now_str}_hash_{hash((now_str, tuple(payload.keys())))}"
    formname = payload.get("formname", None)
    data = dict(
        ref=_hash,
        datetime=now_str,
        formname=formname,
        payload=payload,
        source=payload.get("source")
    )
    store_string("json", f"{_hash}.json", json_dumps(data))
    bottle.response.status = 201
    bottle.response.content_type = "application/json"
    return dict(store="success", ref=_hash)


@app.route("/query", method=["GET", "OPTIONS"])
@app.route("/query/", method=["GET", "OPTIONS"])
@app.route("/query/<file:path>", method=["GET", "OPTIONS"])
@enable_cors
def query(*args, file="", **kwargs):
    bottle.response.status = 200
    bottle.response.content_type = "application/json"
    return query_storage(file)
