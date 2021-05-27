import PySimpleGUI as sg 
from src.Controllers import config_theme as theme

def build():
    layout=[[sg.Text('Aqui se trataran las estadisticas del juego',pad=(190, 0),font= [theme.FONT, 10])],
        [sg.Button('Retornar', k= '-OK-',font= [theme.FONT, 10]) ] ]
    window=sg.Window('Estadisticas' , layout , size= (700, 340))
    return window