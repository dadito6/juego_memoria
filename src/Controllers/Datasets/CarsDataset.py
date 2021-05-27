import csv

from src.Controllers.Datasets.Datasets import cars_path

"""
Todo lo relacionado al control del dataset de los autos va aca
"""


def cars_in_csv():
    """Trae los autos del archivo y los devuelve en formato de lista"""
    datos = []
    with open(cars_path()) as file_cars:
        cars = csv.reader(file_cars, delimiter=',')
        next(cars)
        for elem in cars:
            datos.append(elem)
    return datos


def sort_cars_by_rating():
    """hace un sort de la lista por ranking de autos"""
    return sorted(cars_in_csv(), key=lambda x: int(x[0]))
