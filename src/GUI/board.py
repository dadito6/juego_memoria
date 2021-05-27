import PySimpleGUI as sg
from src.Controllers import config_theme as theme

def frame_info():
    layout = [
        [sg.Text('Nombre de usuario', font = [theme.FONT, 12])],
        [sg.Text('Tiempo restante', font = [theme.FONT, 12])],
        [sg.Button('Salir del juego', key= '-EXIT-', font = [theme.FONT, 12])]
    ]

    return sg.Column(layout, element_justification= 'Right', vertical_alignment= 'b', pad= ((30, 10), 10))

def frame_tablero(matriz):
    layout = [
        [sg.Button(f'{matriz[row][col]}', key=f"cell-{row}-{col}", size=(10, 5), font = [theme.FONT, 12], pad= (5, 5)) for col in range(len(matriz[0]))] for row in range(len(matriz))
    ]
    return sg.Frame('', layout, pad= (5, 5), border_width= 3, background_color= theme.PRIMARY_COLOR_VARIANT)


"""Se crea el tablero con la matriz obetnida anteriormente """
def build(matriz):


    layout = [
        [frame_tablero(matriz), frame_info()]
    ]

    Window = sg.Window('', layout, no_titlebar= True)
    return Window