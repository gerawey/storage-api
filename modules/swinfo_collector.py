import json
from datetime import datetime
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)

def add_switch(switch_id = None, serial_number = None, model = None, ports = None, description = None):
    almacenable = {
        "switch_id": switch_id,
        "serial_number": serial_number,
        "model": model,
        "ports": ports,
        "description": description
    }
    nombre_de_archivo = f"{switch_id}-{serial_number}.json"
    datos = store_string(
        "switch",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_switch_all(switch=None):
    query_result = query_storage(
        "switch",
    )
    if switch is None:
        return query_result["content"]

def switch_by_id(switch_id=None):
    query_result = query_storage(
        "switch",
    )
    if switch_id is not None:
        return [
           r
           for r in query_result["content"]
           if switch_id in r
        ]
    print("Hecho")

def update_switch(switch_id = None, serial_number = None, model = None, ports = None, description = None):
    almacenable = {
        "switch_id": switch_id,
        "serial_number": serial_number,
        "model": model,
        "ports": ports,
        "description": description
        }
    nombre_de_archivo = f"{switch_id}-{serial_number}.json"
    datos = store_string(
        "switch",
        nombre_de_archivo,
        json.dumps(almacenable),
        update=True
    )
    return datos

def add_connect(connect_id = None, switch_in_id = None, switch_out_id = None, port_in = None, port_out = None):
    almacenable = {
        "connect_id": connect_id,
        "switch_in_id": switch_in_id,
        "switch_out_id": switch_out_id,
        "port_in": port_in,
        "port_out": port_out,
    }
    nombre_de_archivo = f"{connect_id}.json"
    datos = store_string(
        "connect",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return False

def get_connect_all(switch=None):
    query_result = query_storage(
        "connect",
    )
    if switch is None:
        return query_result["content"]

def connect_by_id(connect_id=None):
    query_result = query_storage(
        "/connect/<connect_id>",
    )
    if connect_id is not None:
        return [
           r
           for r in query_result["content"]
           if connect_id in r
        ]
    print("Hecho")
