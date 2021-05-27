import PySimpleGUI as sg
from src.GUI import settings
from src.Controllers import Usuario

"""Configuraciones de la ventana de configuracion"""


def start(username):
    window = loop(username)
    window.close()


def loop(username):
    window = settings.build()
    datos = {}
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'EXIT', '-CANCEL_SETTINGS-'):
            break            
            
        if event == '-APPLY_SETTINGS-':
            window.hide()
            datos["level"] = values['-LEVEL-']
            datos["coincidences"] = values['-COINCIDENCES-']
            datos["help"] = 'yes' if values['-CLUES_YES-'] else 'no'
            datos["elements"] = 'words' if values['-WORDS-'] else 'words and images'
            datos["theme"] = 'MemPy ' + values['-THEME-']
            datos["time"] = { 'hours' : values['-HOURS-'], 'minutes' : values['-MINUTES-'], 'seconds' : values['-SECONDS-'] }
            datos_usuario = Usuario.get_datos_usuario(username)
            datos_usuario['config'] = datos
            Usuario.actualizar_usuarios(username, datos_usuario)
            break

        if event == '-RESTORE_DEFAULT_CFG-':
            datos_usuario = Usuario.get_datos_usuario(username)
            datos_usuario = Usuario.set_config_default(datos_usuario)
            Usuario.actualizar_usuarios(username, datos_usuario)
    return window
