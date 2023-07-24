# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:22:09 2022

@author: Sabrina
"""

#Escriba un programa en Python donde cree una lista con 15 elementos aleatorios entre 0 y 9.
#Informe la cantidad de números únicos que contiene (sin repeticiones).
from random import randint
lista1=[]
contador=0
for i in range (0,15):
    lista1.append(randint(0,9))
    if i == lista1[i]:
        contador+=1
print ("La lista es: ", lista1)
print("La cantidad de veces que aparecen numeros unicos es:", contador)