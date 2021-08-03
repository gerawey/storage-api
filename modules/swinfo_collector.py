from os import environ, urandom
import hashlib
from bottle import response, request
import jwt
import binascii
from functools import wraps
import models.auth as mauth







import json
from modules.storage import *

#
# ...
#

def add_switch(id_switch=None, serial_number=None, model=None, ports=None, description=None):
    print("Desde modulo add_switch")
    print(serial_number, model, ports, description)
    para_almacenar = {"id_switch": id_switch,"serial_number": serial_number, "model": model, "ports":ports, "description":description }
    nombre_de_archivo = f"{id_switch}-{title}.json"
    datos = store_string(
        "mi-carpeta3",
        nombre_de_archivo,
        json.dumps(para_almacenar)
    )
    return "Exito"








def add_connect(id_connect=None, switch_in_id=None, switch_out_id=None, port_in=None, port_out=None, description=None):
    print("Desde modulo almacenar_cheat")
    #print(nombre, eda)
    para_almacenar = {"id_connect": id_connect,"switch_in_id": switch_in_id, "switch_out_id": switch_out_id, "port_in":port_in, "port_out":port_out, "description":description }
    json_text = json.dumps(para_almacenar)
    store_string('mi-carpeta', nombre, para_almacenar)
    return "Exito"






