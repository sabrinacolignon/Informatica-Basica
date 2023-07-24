# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:55:11 2022

@author: Sabrina
"""

#Se ingresan el año (int) y luego 12 temperaturas máximas (float) de cada mes registradas en un año en una localidad.
#Los 10 años analizados van entre 1990 y 1999. Organice la información en una estructura de datos,
#determine e informe:
#a) El año de mayor temperatura máxima en febrero. Crear una función.
#b) Qué % disminuyó la temperatura máxima  entre el valor de Enero y el de Julio de 1995. Crear una función.
#c) El promedio de las seis temperaturas máximas en todo el año 1991.

import random as r

def mayor_temp_max(lista, mes):
    maxima=lista[0][mes-1]
    anio=0
    for i in range(len(lista)):
        if maxima>lista[i][mes-1]:
            maxima=lista[i][mes-1]
            anio=i
    return maxima, anio

def disminucion_temp_max(lista, mes1, mes2, anio):
    porcentaje=round((lista[anio-1990][mes1-1]-lista[anio-1990][mes2-1])/100,2)
    return porcentaje

def promedio_6_temp_max(lista, anio):
    max_temp=lista[anio-1990]
    max_temp.sort(reverse=True)
    prom=sum(max_temp[:6])/6
    return prom

temperaturas=[]
for i in range(10):
    temp_max=[]
    for j in range(12):
        temp_medidas=r.randint(1,50)
        temp_max.append(temp_medidas)
    temperaturas.append(temp_max)
    
maxima,anio=mayor_temp_max(temperaturas, 2)
print("El año de mayor temperatura maxima en febrero fue de: ", maxima, "° en el año: ", 1990+anio)
print("El porcentaje que disminuyo la temperatura maxima entre enero y julio de 1995 es de:", disminucion_temp_max(temperaturas, 1, 7, 1995))
print("El promedio de las 6 temperaturas maximas en todo 1991 fue de: ", promedio_6_temp_max(temperaturas, 1991))