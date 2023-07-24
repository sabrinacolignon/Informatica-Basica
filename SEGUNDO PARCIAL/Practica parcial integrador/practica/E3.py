# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:52:45 2022

@author: Sabrina
"""

# El archivo ECG.txt contiene 10000 valores registrados por un cardiólogo mediante un electrocardiograma.
# Lea el archivo ECG.txt y obtenga el promedio de los datos y cuántos valores superan un umbral (umbral = 20 * promedio).

with open ("ECG.txt", "r") as archivo:
    ecg=archivo.readlines()
    
ecg=list(map(int, ecg))
promedio=sum(ecg)//len(ecg)
umbral=20*promedio
contador=0
for dato in ecg:
    if dato>umbral:
        contador+=1
print(contador)