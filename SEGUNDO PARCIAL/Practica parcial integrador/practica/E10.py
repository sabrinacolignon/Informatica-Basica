# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:52:05 2022

@author: Sabrina
"""

# Implemente la función Eliminar Palabra(..) la cual recibe dos cadena, cl y c2. La función busca dentro de c1 la
# ocurrencia de la cadena c2 y la elimina, devolviendo la cadena cl modificada. Si no encuentra c2 devuelve NULL.

def elimina_palabra(cadena1, cadena2):
    if cadena2 in cadena1:
        cadena1=cadena1.replace(cadena2, "")
    else:
        cadena1="NULL"
    return cadena1

cadena1="hola como estas"
cadena2="como"
print(elimina_palabra(cadena1, cadena2))