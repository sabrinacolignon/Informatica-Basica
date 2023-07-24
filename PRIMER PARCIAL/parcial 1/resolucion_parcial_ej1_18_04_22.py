# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:54:28 2022

@author: Sabrina
"""

lista=[]
for i in range(20):
    nombre=input("ingrese nombre del atleta: ")
    numero=input("ingrese numero del atleta: ")
    pais=input("ingrese pais del atleta: ")
    lista.append((nombre, numero, pais))
marcas=[]
for i in range(20):
    print("ingrese mejor marca del atleta ", lista[i])
    m=float(input("ingrese marca del atleta: "))
    marcas.append(m)
M=max(marcas)
i=marcas.index(M)
print("el mejor de la lista es: ", lista[i])
contador=0
for m in marcas:
    if m>=3:
        contador+=1
print("la cantidad de atletas que superaron los 3m fueron: ", contador