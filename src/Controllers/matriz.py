import random

from src.Controllers.Datasets.ManejoHorarios import con_que_se_juega


def procesar_matriz(matriz):
    """Este es el procedimiento para convertir a enteros los valores"""
    x = matriz.split('x')
    return [int(i) for i in x]


TAMANO = procesar_matriz('4x6') 


def lista_preliminar(ocurrencias):
    cont_general = 0
    datos = con_que_se_juega()
    lista_temp = []
    for i in datos:
        count = 0
        if cont_general == TAMANO[0] * TAMANO[1]:
            break
        while count <= ocurrencias:
            lista_temp.append(i[0].rstrip())
            count += 1
            cont_general += 1
    random.shuffle(lista_temp)
    return lista_temp


def rellenar_matriz(matriz, ocurrencia):
    """"En esta funcion se crea la matriz que luego sera utilizada"""
    procesar_matriz(matriz)
    lista = lista_preliminar(ocurrencia)
    chunk_sz = int(len(lista) / TAMANO[0])
    return [lista[i:i + chunk_sz] for i in range(0, len(lista), chunk_sz)]
