# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:47:18 2022

@author: Sabrina
"""

#Escribir un programa en Python que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra=input("Ingrese palabra: ")
if str(palabra)==str(palabra)[::-1] :
    print("La palabra es palíndromo")
else:
    print("La palabra no es palíndromo")