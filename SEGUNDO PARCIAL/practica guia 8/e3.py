# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:06:05 2022

@author: Sabrina
"""

# El archivo ECG.txt contiene 10000 valores registrados por un cardiólogo mediante un electrocardiograma.
# Lea el archivo ECG.txt y obtenga el promedio de los datos y cuántos valores superan un umbral
# (umbral = 20 * promedio).

with open ("ECG.txt", "r") as archivo:
    informacion=archivo.readlines()

datos=list(map(int, informacion))
prom=sum(datos)/len(datos)
contador=0
for dato in datos:
    if dato>(20*prom):
        contador+=1
print("superan el umbral: ", contador)