# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:17:17 2022

@author: Sabrina
"""

# Diseñe e implemente un programa en Python que ordene una lista con 10 valores de manera creciente 
#y lo muestre por pantalla
from random import randint
lista1=[]
for i in range(10):
    lista1.append(randint(1,10))
lista1.sort()
print("la lista ordenada es: ",lista1)