import PySimpleGUI as sg
from src.GUI import estadisticas
from src.Controllers import config_theme as theme

def start():
    window = loop()
    window.close()


def loop():
    window = estadisticas.build()
    while True:
        
        event, values = window.read()
        if event in (sg.WIN_CLOSED,'-CANCEL-'):
            break
        if event == "-OK-":
            break
            
            
        
    return window