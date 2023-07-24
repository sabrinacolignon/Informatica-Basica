# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:52:23 2022

@author: Sabrina
"""

# Escriba una función C++ llamada Insertar con 3 parámetros: cad1, cad2, i que permita insertar cad2 en cad1 a partir de
# la posición i de cad1. La función debe modificar cad1. Por ejemplo: si cad1 contiene el string "El libro" y cad2 el
# string "primer", la llamada a Insertar(cad1, cad2,4) debe lograr que cad1 almacene "El pimer libro". 

def inserta_palabra(cad1, cad2, indice):
    separa_c1=cadena1.split(" ")
    separa_c1.insert(indice, cadena2)
    cadena_final=' '.join(separa_c1)
    return cadena_final

cadena1="el libro"
cadena2="primer"
indice=1

print(inserta_palabra(cadena1, cadena2, indice))
