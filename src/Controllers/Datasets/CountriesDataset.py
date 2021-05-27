import csv

from src.Controllers.Datasets.Datasets import countries_path

"""
Todo lo relacionado al control del dataset de los paises va aca
"""


def countries_in_csv():
    """Trae los paises del archivo y los devuelve en formato de lista"""
    datos = []
    with open(countries_path()) as file_country:
        countries = csv.reader(file_country, delimiter=',')
        next(countries)
        for elem in countries:
            datos.append(elem)
    return datos



def sort_por_nombre():
    """hace un sort de la lista por nombre de pais"""
    return sorted(countries_in_csv(), reverse=False, key=lambda x: x[0])


def sort_por_poblacion():
    """Poblacion descendente"""
    return sorted(countries_in_csv(), reverse=True, key=lambda x: int(x[2]))


def sort_por_area():
    """En millas^2 descendente"""
    return sorted(countries_in_csv(), reverse=True, key=lambda x: float(x[3]))


def sort_por_gdp():
    """Orden por gdp"""
    return sorted(countries_in_csv(), key=lambda x: int(x[8]) if x[8].isdigit() else -1, reverse=True)


def paises_europeos():
    """Paises europeos"""
    lista_a_devolver = []
    for linea in sort_por_nombre():
        if europa(linea):
            aux = str.rstrip(linea[0])
            lista_a_devolver.append(aux)
    return lista_a_devolver


def paises_latinos():
    """Paises Latinos"""
    lista_a_devolver = []
    for linea in sort_por_nombre():
        if latam(linea):
            aux = str.rstrip(linea[0])
            lista_a_devolver.append(aux)
    return lista_a_devolver


def paises_asiaticos_oceania():
    """Paises Asiaticos y de Oceania"""
    lista_a_devolver = []
    for linea in sort_por_nombre():
        if asia_oceania(linea):
            aux = str.rstrip(linea[0])
            lista_a_devolver.append(aux)
    return lista_a_devolver


def europa(line):
    return 'EUROPE' in line[1]


def latam(line):
    return 'LATIN AMER' in line[1]


def asia_oceania(line):
    return 'ASIA' in line[1] or 'OCEANIA' in line[1]


def countries_dataset(dia_de_juego):
    """Viene un dia para jugar por parametro y segun lo que surja se devuelve los datos sorteados de X forma"""
    if dia_de_juego == 0:
        return sort_por_nombre()
    if dia_de_juego == 1:
        return sort_por_poblacion()
    if dia_de_juego == 2:
        return sort_por_area()
    if dia_de_juego == 3:
        return sort_por_gdp()
    if dia_de_juego == 4:
        return paises_europeos()
    if dia_de_juego == 5:
        return paises_latinos()
    if dia_de_juego == 6:
        return paises_asiaticos_oceania()

