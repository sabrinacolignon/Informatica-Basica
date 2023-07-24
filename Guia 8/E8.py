# -*- coding: utf-8 -*-
"""
Created on Wed May 11 18:26:59 2022

@author: Sabrina
"""

#En el archivo covid.csv se encuentran almacenados los datos de casos COVID de diez países. Lea el archivo y
#determine el ranking de los 5 países más comprometidos actualmente (con mayor casos activos) y escriba dicho
#ranking en un archivo csv llamado Ranking5Covid.txt.

import csv
import operator as op

covid=[]
with open("covid.csv", "r") as archivo:
    lector=csv.reader(archivo, delimiter=',')
    columnas=next(lector)
    for linea in lector:
        covid.append([linea[0], int(linea[1]), int(linea[2]), int(linea[3]), int(linea[4])])
        
covid.sort(key=op.itemgetter(4), reverse=True)#ordeno por la 4ta columna

with open("Ranking5Covid.txt", "w") as arch_es:
    escritor=csv.writer(arch_es, delimiter=";")
    escritor.writerow(columnas)
    escritor.writerows(covid[:5])
    