# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:58:15 2022

@author: Sabrina
"""

#7. Se ingresan el año (int) y luego 12 temperaturas máximas (float) de cada mes registradas en un año
#en una localidad.  Los 10 años analizados van entre 1990 y 1999. Organice la información en una
#estructura de datos, determine e informe:
#a) El año de mayor temperatura máxima en febrero. Crear una función.
#b) Qué % disminuyó la temperatura máxima entre el valor de Enero y el de Julio de 1995.
    #Crear una función.
#c) El promedio de las 6 temperaturas máximas en todo el año 1991.
import random as r

def max_temp_feb(x, mes):
    Max_t=x[0][mes-1]
    anio=0
    for i in range(len(x)):
        if x[i][mes-1]>Max_t:
            Max_t=x[i][mes-1]
            anio=i
    return anio #me conforma una tupla si devuelvo dos resultados, si quiero que sea una lista, le pongo corchetes

def porcentaje_disminucion(x, anio, mes1, mes2):
    max_temp_mes1=x[anio-1990][mes1-1]
    max_temp_mes2=x[anio-1990][mes2-1]
    resta=max_temp_mes2-max_temp_mes1
    porcentaje=round(resta/100,2)
    return porcentaje

def promedio_temp_max(datos, anio):
    x=datos[anio-1990]
    x.sort(reverse=True)
    prom=sum(x[:6])/6
    return prom

temp=[]
for i in range (10):
    fila=[]
    for j in range(12):
        #dato=float(input("ingrese la temperatura del mes " + str(j+1) + "del año: " + str(1990+i)))
        dato=r.randint(1,45)
        fila.append(dato)
    temp.append(fila)

anio_max_temp_feb=max_temp_feb(temp, 2)
print("El año de mayor temperatura en febrero es: ", 1990+anio_max_temp_feb)

porcentaje=porcentaje_disminucion(temp, 1995, 1, 7)
print("El porcentaje que disminuyó la temperatura máxima entre el valor de Enero y el de Julio de 1995 es de: ", porcentaje)

prom=promedio_temp_max(temp, 1991)
print("El promedio de las 6 temperaturas máximas en todo el año 1991 es: ", prom)
