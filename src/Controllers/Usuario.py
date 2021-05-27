import json
import os

"""Manejo del usuario"""

FILE_NAME = 'users.json'
PATH_FILE = os.path.join(os.getcwd(), 'src', 'Entities', FILE_NAME)


def traer_usuarios_a_lista(diccionario):
    """Recibe el json de los usuario y devuelve las keys en formato de lista"""
    return list(diccionario.keys())


def cargar_usuarios():
    """Abre el json y lo trae en diccionario"""
    with open(PATH_FILE, 'r') as f:
        dicc = json.load(f)
    return dicc


def guardar_usuarios(datos):
    """abre el json y guarda el usuario"""
    with open(PATH_FILE, 'w') as f:
        json.dump(datos, f, indent=4)


def actualizar_usuarios(username, values):
    """actualiza el usuario"""
    datos = cargar_usuarios()
    datos[username] = values
    guardar_usuarios(datos)

def get_datos_usuario(username):
    """Retorna datos del usuario indicado por parámetro"""

    datos = cargar_usuarios()
    return datos[username]


def set_config_default(values):
    """le carga a un usuario nuevo los valores defaults"""
    datos = cargar_usuarios()
    values["config"] = datos["default"]["config"]
    return values
