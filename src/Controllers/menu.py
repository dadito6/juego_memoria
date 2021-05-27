import PySimpleGUI as sg
from src.GUI import menu
from src.Controllers import settings , estadisticas, highscores,board

"""Archivo con la logica del menu"""

def start(username):
    window = loop(username)
    window.close()


def loop(username):
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window = menu.build()
    while True:
        event, _values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break
        if event == "-play-":
            window.hide()
            board.start(username)
            window.un_hide()
        if event == "-settings-":    
            window.hide()
            settings.start(username)
            window.un_hide()
        if event == "-score-":
            highscores.start()
        if event == '-stats-':
            estadisticas.start()
            

    return window