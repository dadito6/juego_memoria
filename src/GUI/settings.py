import PySimpleGUI as sg

from src.Controllers import config_theme as theme

"""Construccion de la ventana de settings"""


def mensajes_a_mostrar():
    """ Seccion Mensajes de victoria/derrota/y el tiempo a poner"""
    layout = [
        sg.Text('Mensajes a mostrar:', font=[theme.FONT, 12], background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Checkbox('Victoria', default=True, k='-WIN_MSG-', font=[theme.FONT, 12],
                    background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Checkbox('Derrota', default=True, k='-LOSE_MSG-', font=[theme.FONT, 12],
                    background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Checkbox('Tiempo restante', default=True, k='-TIME_MSG-', font=[theme.FONT, 12],
                    background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6))
    ]
    return layout


def casillas_tablero():
    """ Seccion tamaño tablero"""
    values = ('3x3', '6x6', '8x8')
    layout = [
        sg.Text('Casillas del tablero: ', font=[theme.FONT, 12], background_color=theme.PRIMARY_COLOR_VARIANT,
                pad=(5, 6)),
        sg.Combo(values, default_value=values[0], font=[theme.FONT, 12], key='-LEVEL-', pad=(5, 6))
    ]

    return layout


def coincidencias_elemento():
    """ Seccion con cuantas fichas jugar"""
    values = [x for x in range(2, 100)]

    layout = [
        sg.Text('Coincidencias por elemento: ', font=[theme.FONT, 12], background_color=theme.PRIMARY_COLOR_VARIANT,
                pad=(5, 6)),
        sg.Spin(values, initial_value=2, key='-COINCIDENCES-', font=[theme.FONT, 12], pad=(5, 6))
    ]

    return layout


def tipo_elementos():
    """ Seccion jugar con imagenes y/o texto"""
    layout = [
        sg.Text('Tipos de elementos de las casillas: ', font=[theme.FONT, 12],
                background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Radio('Palabras', '-ELEMENTS-', True, key='-WORDS-', font=[theme.FONT, 12],
                 background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Radio('Imágenes y palabras', '-ELEMENTS-', key='-IMAGES-', font=[theme.FONT, 12],
                 background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6))
    ]

    return layout


def mostrar_pistas():
    """ Seccion mostrar pistas para jugar"""
    layout = [
        sg.Text('Pistas: ', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12], pad=(5, 6)),
        sg.Radio('Sí', '-HELP-', default=True, key='-CLUES_YES-', background_color=theme.PRIMARY_COLOR_VARIANT,
                 font=[theme.FONT, 12], pad=(5, 6)),
        sg.Radio('No', '-HELP-', key='-CLUES_NO-', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12],
                 pad=(5, 6))
    ]

    return layout


def tiempo_partida():
    """ Seccion tiempo de la partida"""
    horas = [x for x in range(0, 100)]
    min_seg = [x for x in range(0, 60)]

    layout = [
        sg.Text('Tiempo total de la partida:', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12],
                pad=(5, 6)),
        sg.Spin(horas, initial_value=0, key='-HOURS-', font=[theme.FONT, 12], pad=(5, 6)),
        sg.Text(':', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12], pad=(5, 6)),
        sg.Spin(min_seg, initial_value=10, key='-MINUTES-', font=[theme.FONT, 12], pad=(5, 6)),
        sg.Text(':', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12], pad=(5, 6)),
        sg.Spin(min_seg, initial_value=0, key='-SECONDS-', font=[theme.FONT, 12], pad=(5, 6))
    ]

    return layout


def seleccionar_tema():
    """ Theme a elegir para el programa"""
    values = ('Light Green', 'Light Red', 'Light Blue', 'Dark Green', 'Dark Red', 'Dark Blue')

    layout = [
        sg.Text('Tema: ', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12], pad=(5, 6)),
        sg.Combo(values, default_value='Light Green', key='-THEME-', font=[theme.FONT, 12], pad=(5, 6))
    ]

    return layout


def build():
    """Construccion final de la ventana"""
    settings_dificultad = [
        casillas_tablero(),
        coincidencias_elemento(),
        mostrar_pistas(),
        tiempo_partida(),
    ]

    settings_otros = [
        mensajes_a_mostrar(),
        tipo_elementos(),
        seleccionar_tema()
    ]

    tab_dificultad = sg.Tab('Dificultad', settings_dificultad, font=[theme.FONT, 12],
                            background_color=theme.PRIMARY_COLOR_VARIANT, title_color='Black',
                            element_justification='c')
    tab_otros = sg.Tab('Otros', settings_otros, font=[theme.FONT, 12], background_color=theme.PRIMARY_COLOR_VARIANT,
                       title_color='White', element_justification='c')
    layout_tabs = [[tab_dificultad, tab_otros]]

    layout = [
        [sg.Text('Configuración', background_color=theme.PRIMARY_COLOR, font=[theme.FONT, 30], pad=(90, 5))],
        [sg.TabGroup(layout_tabs, 'top', background_color=theme.PRIMARY_COLOR, font=[theme.FONT, 15],
                     title_color='Black', tab_background_color=theme.PRIMARY_COLOR_VARIANT,
                     selected_background_color=theme.PRIMARY_COLOR, pad=((100, 50), 0))],
        [sg.Button('Restaurar a valores por defecto', key="-RESTORE_DEFAULT_CFG-", font=[theme.FONT, 12], pad=(0, 10))],
        [sg.Button('Cancelar', key='-CANCEL_SETTINGS-', font=[theme.FONT, 15], pad=((0, 5), 10)),
         sg.Button('Aplicar cambios', key='-APPLY_SETTINGS-', font=[theme.FONT, 15], pad=((5, 0), 10)), ]

    ]

    return sg.Window('Configuración', margins=(0, 0), no_titlebar=True, background_color=theme.PRIMARY_COLOR,
                     element_justification='c', finalize=True, grab_anywhere=True).Layout(layout)
