# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:24:17 2022

@author: Sabrina
"""

# Una empresa fabricante de equipos para medicina exporta a 9 paises y desea analizar el desempeño de las ventas
# en el año 2021. Para ello se dispone de un archivo de textos EXPORT2021.CSV donde se encuentran almacenados en
# cada línea 3 datos (separados por comas por cada operación de venta por exportación realizada en ese año:
# cod. equipo (1..9), fecha (aaaammdd), monto de la venta. Puede haber varias ventas de un mismo equipo en un mismo mes.
# La fecha es un número de 8 cifras: las primeras 4 el año, las 2 siguientes el mes, luego el día.
# a) Organice una matriz de 9 filas (equipos) x 12 columnas (meses), y en cada celda acumule los montos resultante
#     de las ventas en 2021.
# b) A través de una función determine la recaudación anual por ventas del equipo 7
# c) Con una función determine cuál fue el mayor monto de venta del mes de junio y a cuál equipo corresponde.
#     Informe los resultados de byc.
import csv

def recaudacion_anual(lista, cod_equipo):
    recaudacion=0
    for i in range(len(lista)):
        recaudacion+=lista[cod_equipo-1][i]
    return recaudacion

def mayor_recaudacion(lista, mes):
    max_rec=lista[0][mes-1]
    for i in range(1,len(lista)):
        if max_rec<lista[i][mes-1]:
            max_rec=lista[i][mes-1]
            equipo_max_rec=i+1
    return max_rec, equipo_max_rec

ventas=[[0]*12 for i in range(9)]
with open ("EXPORT2021.CSV", "r") as archivo:
    lector=csv.reader(archivo, delimiter=',')
    for linea in lector:
        cod_equipo=int(linea[0])
        mes=int(linea[1]//10000)%100
        monto=float(linea[2])
        ventas[cod_equipo-1][mes-1]+=monto