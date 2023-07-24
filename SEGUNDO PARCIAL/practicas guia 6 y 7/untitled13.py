# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:29:20 2022

@author: Sabrina
"""

# Se ingresan el año (int) y luego 12 temperaturas máximas (float) de cada mes registradas en un año en una localidad.
# Los 10 años analizados van entre 1990 y 1999. Organice la información en una estructura de datos,
# determine e informe:
# a) El año de mayor temperatura máxima en febrero. Crear una función.
# b) Qué % disminuyó la temperatura máxima  entre el valor de Enero y el de Julio de 1995. Crear una función.
# c) El promedio de las seis temperaturas máximas en todo el año 1991.
import random as r

def mayor_temp_maxim(lista, mes):
    anio=0
    mayor_temp=lista[0][0]
    for i in range(len(lista)):
        if mayor_temp>lista[i][mes-1]:
            mayor=lista[i][mes-1]
            anio=i
    return mayor, anio

def promedio_dism_temp(lista, mes1, mes2, anio):
    prom=round((lista[mes2-1][anio-1990]-lista[mes1-1][anio-1990])/100,2)
    return prom

def promedio_6_temp_max(lista, anio):
    max_temp=lista[anio-1990]
    max_temp.sort(reverse=True)
    prom=sum(max_temp[:6])/6
    return prom

temperaturas=[]
for i in range(10):
    temp_maximas=[]
    for j in range(12):
        temp=r.randint(1,50)
        temp_maximas.append(temp)
    temperaturas.append(temp_maximas)
