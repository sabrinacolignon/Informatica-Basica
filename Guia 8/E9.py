# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:38:01 2022

@author: Sabrina
"""

# El archivo CP.csv contiene 256 registros (filas) correspondientes a los valores de los cuatro sensores de presión
# de una plataforma Wii durante la realización de un experimento sobre balance estático (4 valores por cada fila).
# Utilice un programa en para leer el archivo y obtener la evolución del centro de presiones en el eje x (CPx) y en 
# el eje y (CPy). Para ello utilice las siguientes fórmulas: donde M(i,1) es el valor del sensor 1 de la fila i, 
# M(i,2) el valor del sensor 2 de la fila i, etc. Por cada fila de CP.csv se obtiene un par de valores CPx y CPy.
# Genere un nuevo archivo llamado Desplazamientos.txt que en cada fila contenga este par de valores.
import csv

registros=[]
centro_presiones=[]
with open ("CP.csv", "r") as archivo:
    interprete=csv.reader(archivo, delimiter=',')
    for linea in interprete:
        registros.append([int(linea[0]), int(linea[1]), int(linea[2]), int(linea[3])])
for i in range(len(registros)):
    CPx=(433/2)*((registros[i][2]+registros[i][3])-(registros[i][0]+registros[i][1]))/(registros[i][0]+registros[i][1]+registros[i][2]+registros[i][3])
    CPy=(238/2)*((registros[i][0]+registros[i][2])-(registros[i][1]+registros[i][3]))/(registros[i][0]+registros[i][1]+registros[i][2]+registros[i][3])
    centro_presiones.append([CPx, CPy])

with open ("Desplazamientos.txt", "w") as nuevo_archivo:
    escritor=csv.writer(nuevo_archivo, delimiter=',')
    escritor.writerows(centro_presiones)