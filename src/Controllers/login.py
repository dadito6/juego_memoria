import PySimpleGUI as sg
from src.GUI import login
from src.Controllers import Usuario, menu, registro, config_theme as theme

"""Toda la logica del login va aca"""


def start():
    window = loop()
    window.close()


def loop():
    diccionario = Usuario.cargar_usuarios()
    nicknames = Usuario.traer_usuarios_a_lista(diccionario)
    window = login.build()
    while True:
        
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-CANCEL-'):
            break
        if event == "-OK-":
            if values["-USERNAME-"].lower() in nicknames:
                window.hide()
                menu.start(values["-USERNAME-"].lower())
                break
            else:
                sg.popup("failed, try again", background_color= theme.PRIMARY_COLOR_VARIANT, no_titlebar= True)
        if event == '-REGISTER-':
            window.hide()
            registro.start(nicknames)
            break
        
    return window