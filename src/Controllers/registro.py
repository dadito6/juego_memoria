import PySimpleGUI as sg
from src.GUI import registro
from src.Controllers import Usuario, login, menu

"""La logica del registro va aca"""


def start(nicknames):
    window = loop(nicknames)
    window.close()


def loop(nicknames):
    window = registro.build()

    datos_usuario = {}
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-CANCEL-'):
            break
        if event == "-USERNAME-":
            username = values.get('-USERNAME-')
            if username.lower() in nicknames or len(username) == 0:
                window["-OK-"].update(visible=False)
                window["-LOGIN-"].update(visible=True)
                window["-ERROR-"].update(visible=True)
            else:
                window["-OK-"].update(visible=True)
                window["-LOGIN-"].update(visible=False)
                window["-ERROR-"].update(visible=False)
        if event == '-OK-':
            username = values['-USERNAME-'].lower()
            datos_usuario['age'] = values['-AGE-']
            datos_usuario['gender'] = values['-GENDER-'].lower()
            datos_usuario = Usuario.set_config_default(datos_usuario)
            Usuario.actualizar_usuarios(username, datos_usuario)
            window.hide()
            menu.start(username)
            break
        if event == '-LOGIN-':
            window.hide()
            login.start()
            break

    return window
