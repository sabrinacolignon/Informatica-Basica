# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:17:44 2022

@author: Sabrina
"""

#Escribir un programa en Python que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
cadena=input("Ingrese cadena: ")
if str(cadena)==str(cadena)[::-1]:#invierte la cadena
    print("Es un palíndromo")
else:
    print("No es palíndromo")