# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:09:58 2022

@author: Sabrina
"""

#El archivo ECG.txt contiene 10.000 valores registrados por un cardiólogo mediante un electrocardiograma.
#Lea el archivo ECG.txt y obtenga el promedio de los datos y cuántos valores superan un umbral
#(umbral = 20 * promedio).
with open("ECG.txt", "r") as archi:
    info=archi.readlines()
registro=[]
for i in range(len(info)):
    registro.append(int(info[i]))
acum=0
contador=0
for i in range(len(registro)):
    acum+=i
    promedio=acum/10000
    umbral=20*promedio
    if registro[i]>umbral:
        contador+=1
print("La cantidad de valores que superaron el umbral fueron: ", contador)
archi.close()