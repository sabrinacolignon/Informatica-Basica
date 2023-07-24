# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:57:52 2022

@author: Sabrina
"""

import operaciones_naturales
#si es par o no, si es primo o no, sus divisores y su factorial.
numero=int(input("ingrese numero de prueba: "))
print("el numero que ingreso si es par saldra: True, en el caso opuesto False:")
print(operaciones_naturales.es_par(numero))

print("el numero que ingreso si es primo saldra: True, en el caso opuesto False:")
print(operaciones_naturales.es_primo(numero))

print("los divisores del numero elegido son: ")
print(operaciones_naturales.divisores(numero))

print("el factorial del numero elegido es: ")
print(operaciones_naturales.factorial(numero))