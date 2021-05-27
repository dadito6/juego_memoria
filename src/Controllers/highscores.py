import PySimpleGUI as sg
from src.GUI import highscores


def start():
    window = loop()
    window.close()


def loop():
    window = highscores.build()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-RETURN-'):
            break
    return window