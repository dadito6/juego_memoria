import PySimpleGUI as sg

"""
Muestra de los HIGHSCORES
"""


def build():
    layout = [[sg.Text('HISHSCORES', font='Any 15')],
              [sg.HorizontalSeparator(color='Black')],
              [sg.Text('NOMBRE JUGADOR', font='Any 10', pad=(70, 0)),
               sg.Text('PUNTAJE', font='Any 10', pad=((0, 10), (0, 0)))],
              [sg.Text('TOP 1:', font='Any 10'), sg.Text('ACA IRIA UN USUARIO', justification='center', font='Any 10'),
               sg.Text('ACA IRIA UN PUNTAJE')],
              [sg.Text('TOP 2:', font='Any 10'), sg.Text('ACA IRIA UN USUARIO', justification='center', font='Any 10'),
               sg.Text('ACA IRIA UN PUNTAJE')],
              [sg.Text('TOP 3:', font='Any 10'), sg.Text('ACA IRIA UN USUARIO', justification='center', font='Any 10'),
               sg.Text('ACA IRIA UN PUNTAJE')],
              [sg.Text('TOP 4:', font='Any 10'), sg.Text('ACA IRIA UN USUARIO', justification='center', font='Any 10'),
               sg.Text('ACA IRIA UN PUNTAJE')],
              [sg.Text('TOP 5:', font='Any 10'), sg.Text('ACA IRIA UN USUARIO', justification='center', font='Any 10'),
               sg.Text('ACA IRIA UN PUNTAJE')],
              [sg.Button('Volver al menu', key='-RETURN-')]]
    window = sg.Window('Window Title', layout)

    return window