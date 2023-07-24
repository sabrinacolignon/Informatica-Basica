# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:53:50 2022

@author: Sabrina
"""

nombres=[]
edades=[]
for x in range(5):
    nom=input("Ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed=int(input("Ingrese la edad de dicha persona: "))
    edades.append(ed)

print("Nombre de las personas mayores de edad: ")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])