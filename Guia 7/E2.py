# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:58:12 2022

@author: Sabrina
"""

#Escribir un programa en Python en el que se pregunte al usuario por una frase
#y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase=input("Ingrese una frase: ")
letra=input("Ingrese una letra: ")
contador=0

for i in frase:
  if i==letra:
    contador+=1
    
print("La letra", letra, "aparece", contador, "veces en la frase: ", frase)