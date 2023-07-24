# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:12:15 2022

@author: Sabrina
"""

#Escriba un programa en Python donde cree una lista con los primeros 20 números múltiplos de 3.
#Genere la lista de al menos dos maneras diferentes.
lista1=[]
for i in range(0,20):
    if i%3==0:
        lista1.append(i)
print("la lista 1 es: ", lista1)
print("-------")
lista2=[i for i in range (0, 20) if i%3==0]
print("la lista 2 es: ", lista2)