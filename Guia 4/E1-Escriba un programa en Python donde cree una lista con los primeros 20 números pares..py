# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:00:13 2022

@author: Sabrina
"""
from random import randint
#Escriba un programa en Python donde cree una lista con los primeros 20 números pares.
#Genere la lista de al menos dos maneras diferentes.
lista1=[]

for i in range (0,20):
    if i%2==0:
        lista1.append(i)
print("La lista 1 es: ", lista1)
print("-------")

lista2=[i for i in range(0,21) if i%2==0]
print("La lista2 es: ", lista2)
    