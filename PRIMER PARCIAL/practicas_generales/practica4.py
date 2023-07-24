# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:51:50 2022

@author: Sabrina
"""

lista=[]
for x in range(5):
    valor=int(input("Ingrese valor: "))
    lista.append(valor)

menor=lista[0]
posicion=0
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x+1

print("Lista completa", lista)
print("Menor de la lista", menor)
print("Posicion del menor en la lista", posicion)