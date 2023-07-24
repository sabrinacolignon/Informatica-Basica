# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
lista=[]
for i in range(400):
    lista.append(random.randint(-50,50))
contador=0
for i in range(1, len(lista)):
    p=lista[i]*lista[i-1]
    if p<0:
        contador+=1
print("la cantidad de veces que se cambia de signo: ", contador)