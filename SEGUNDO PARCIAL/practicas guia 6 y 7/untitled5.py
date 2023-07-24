# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:37:06 2022

@author: Sabrina
"""

#Escribir un programa en Python en el que se pregunte al usuario por una frase y una letra,
#y muestre por pantalla el número de veces que aparece la letra en la frase.

frase=input("Ingrese frase: ")
letra=input("Ingrese letra para contar la cantidad de veces que aparece: ")
contador=0
for i in frase:
    if i ==letra:
        contador+=1
print("La letra", letra, "aparece: ", contador, "veces en la frase <", frase,">")