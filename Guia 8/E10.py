# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:04:40 2022

@author: Sabrina
"""

# A partir de los datos de cantidad de consultas médicas realizadas en el país entre los años 2013 a 2018 (5años),
# suministrados por el archivo cantidad-consultas-medicas-ambulatorias.csv, obtenga:
# a- La cantidad total de consultas médicas registradas por año.
# b- Para cada año, qué unidad operativa recibió más consultas y cuántas fueron.
# c- Para cada año, qué unidades operativas recibieron menos de 1000 (mil) consultas médicas.
# Además, realizar un ranking Top 10 con las 10 unidades operativas más consultadas históricamente (desde 2013 a 2018)
# y sus respectivos valores (sumatoria de consultas), almacene este ranking en el archivo Top10Consultas.txt

import csv

def calcula_max_consultas (lista, anio):
    mayor_consultas_op=consultas_medicas[0][anio]
    for i in range(len(lista)):
        if mayor_consultas_op<consultas_medicas[i][anio]:
            mayor_consultas_op=consultas_medicas[i][anio]
            id_cantidad_mayor=i+1
    return id_cantidad_mayor, mayor_consultas_op

def menos_mil_consultas_medicas(lista, anio):
    menos_mil=[]
    for i in range (len(lista)):
        if lista[i][anio]<1000:
            menos_mil.append([i+1])
    return menos_mil

consultas_medicas=[]
with open("cantidad-consultas-medicas-ambulatorias.csv", "r") as archivo:
    lector=csv.reader(archivo, delimiter=',')
    columnas=next(lector)
    for linea in lector:
        #hay otra forma de hacer lo de abajo?
        #puedo ahcer 5 listas por año pero como las separo? del elemento 2 al 7
        consultas_medicas.append([int(linea[0]), linea[1], int(linea[2]), int(linea[3]), int(linea[4]), int(linea[5]), int(linea[6]), int(linea[7])])
print("La cantidad de consultas por año fueron: ", len(consultas_medicas))

#para cada año, que unidad operativa recibio mas consultas y cuantas fueron:
print("Para el año 2013 la unidad operativa que recibio mas consultas y su cantidad fue: ", calcula_max_consultas(consultas_medicas, 2))
print("Para el año 2014 la unidad operativa que recibio mas consultas y su cantidad fue: ", calcula_max_consultas(consultas_medicas, 3))
print("Para el año 2015 la unidad operativa que recibio mas consultas y su cantidad fue: ", calcula_max_consultas(consultas_medicas, 4))
print("Para el año 2016 la unidad operativa que recibio mas consultas y su cantidad fue: ", calcula_max_consultas(consultas_medicas, 5))
print("Para el año 2017 la unidad operativa que recibio mas consultas y su cantidad fue: ", calcula_max_consultas(consultas_medicas, 6))
print("Para el año 2018 la unidad operativa que recibio mas consultas y su cantidad fue: ", calcula_max_consultas(consultas_medicas, 7))
   
#para cada año, que unidades operativas recibieron menos de mil consultas medicas:
print("Para el año 2013 las unidades operativa que recibieron menos de mil consultas fueron: ", menos_mil_consultas_medicas(consultas_medicas, 2))
print("Para el año 2014 las unidades operativa que recibieron menos de mil consultas fueron: ", menos_mil_consultas_medicas(consultas_medicas, 3))
print("Para el año 2015 las unidades operativa que recibieron menos de mil consultas fueron: ", menos_mil_consultas_medicas(consultas_medicas, 4))
print("Para el año 2016 las unidades operativa que recibieron menos de mil consultas fueron: ", menos_mil_consultas_medicas(consultas_medicas, 5))
print("Para el año 2017 las unidades operativa que recibieron menos de mil consultas fueron: ", menos_mil_consultas_medicas(consultas_medicas, 6))
print("Para el año 2018 las unidades operativa que recibieron menos de mil consultas fueron: ", menos_mil_consultas_medicas(consultas_medicas, 7))

#ranking top10 de unidades operativas mas consultadas y sus valores(sumatoria de consultas):
sumatoria_2013=[]
sumatoria=0
for i in range(len(consultas_medicas)):
    sumatoria+=consultas_medicas[i][2]
    sumatoria_2013.append(sumatoria)
sumatoria_2013.sort(reverse=True)

sumatoria_2014=[]
for i in range(len(consultas_medicas)):
    sumatoria+=consultas_medicas[i][3]
    sumatoria_2014.append(sumatoria)
sumatoria_2014.sort(reverse=True)

sumatoria_2015=[]
for i in range(len(consultas_medicas)):
    sumatoria+=consultas_medicas[i][4]
    sumatoria_2015.append(sumatoria)
sumatoria_2015.sort(reverse=True)

sumatoria_2016=[]
for i in range(len(consultas_medicas)):
    sumatoria+=consultas_medicas[i][5]
    sumatoria_2016.append(sumatoria)
sumatoria_2016.sort(reverse=True)

sumatoria_2017=[]
for i in range(len(consultas_medicas)):
    sumatoria+=consultas_medicas[i][6]
    sumatoria_2017.append(sumatoria)
sumatoria_2017.sort(reverse=True)

sumatoria_2018=[]
for i in range(len(consultas_medicas)):
    sumatoria+=consultas_medicas[i][7]
    sumatoria_2018.append(sumatoria)
sumatoria_2018.sort(reverse=True)

with open("Top10Consultas.txt", "w") as nuevo_archivo:
    escritor=csv.writer(nuevo_archivo, delimiter=',')
    escritor.writerow(columnas)
    escritor.writerow(sumatoria_2013[:10])
    escritor.writerow(sumatoria_2014[:10])
    escritor.writerow(sumatoria_2015[:10])
    escritor.writerow(sumatoria_2016[:10])
    escritor.writerow(sumatoria_2017[:10])
    escritor.writerow(sumatoria_2018[:10])
    
    