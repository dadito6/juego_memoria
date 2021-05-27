import PySimpleGUI as sg
from src.GUI import board
from src.Controllers import config_theme as theme, Usuario , matriz
""" Aqui se trabajara la logica del tablero"""

def start(username):
    window = loop(username)
    window.close()


def loop(username):
    datos=Usuario.get_datos_usuario(username)
    level= datos['config']['level']
    ocurrencias=datos['config']['coincidences']
    a= matriz.rellenar_matriz(level,ocurrencias)
    window = board.build(a)
    while True:
        
        event, _values = window.read()
        if event in (sg.WIN_CLOSED,'-CANCEL-', '-EXIT-'):
            break           
            
        
    return window