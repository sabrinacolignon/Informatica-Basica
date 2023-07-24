# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:18:48 2022

@author: Sabrina
"""

# En el archivo covid.txt se encuentran almacenados los datos de casos COVID de diez países.
# Lea el archivo y determine el ranking de los 5 países más comprometidos actualmente (con mayor casos activos)
# y escriba dicho ranking en un archivo csv llamado Ranking5Covid.txt.
import csv
import operator as op

covid=[]
with open ("covid.csv", "r") as archivo:
    interprete=csv.reader(archivo, delimiter=',')
    columnas=next(interprete)
    for linea in interprete:
        covid.append([linea[0], int(linea[1]), int(linea[2]), int(linea[3])])

covid.sort(key=op.itemgetter(3), reverse=True) #ordeno por la 4ta columna

with open("Ranking5Covid.txt", "w") as arch_es:
    escritor=csv.writer(arch_es, delimiter=";")
    escritor.writerow(columnas)
    escritor.writerows(covid[:5])
        