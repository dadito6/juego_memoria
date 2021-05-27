import json
import os
import PySimpleGUI as sg

"""Configuracion de los Themes a ser usados"""

FONT = ""
PRIMARY_COLOR = ""
PRIMARY_COLOR_VARIANT = ""
SECONDARY_COLOR = ""
SECONDARY_COLOR_VARIANT = ""
THEME_DEFAULT = "Light Green"


def cargar_tema(theme_name=THEME_DEFAULT):
    """Carga del tema"""
    theme_name = 'MemPy ' + theme_name
    themes_file = 'themes.json'
    with open(os.path.join(os.getcwd(), 'src', 'Entities', 'Graphics', themes_file), 'r') as t:
        themes = json.load(t)
    try:
        sg.theme_add_new(theme_name, themes[theme_name]["theme_content"])
        sg.change_look_and_feel(theme_name)
        global FONT
        FONT = themes[theme_name]["text_font"]
        global PRIMARY_COLOR
        PRIMARY_COLOR = themes[theme_name]["primary_color"]
        global PRIMARY_COLOR_VARIANT
        PRIMARY_COLOR_VARIANT = themes[theme_name]["primary_color_variant"]
        global SECONDARY_COLOR
        SECONDARY_COLOR = themes[theme_name]["secondary_color"]
        global SECONDARY_COLOR_VARIANT
        SECONDARY_COLOR_VARIANT = themes[theme_name]["secondary_color_variant"]
    except KeyError:
        sg.Popup("No se ha encontrado un tema con dicho nombre")
