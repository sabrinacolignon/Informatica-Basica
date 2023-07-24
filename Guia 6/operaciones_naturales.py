# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:41:33 2022

@author: Sabrina
"""

#Construya el módulo operaciones_naturales.py, este debe contener las funciones: es_par(numero), divisores(numero),
#es_primo(numero) y factorial(numero), diseñadas e implementadas en los ejercicios previos y ejemplos.
#Diseñe e implemente un programa en Python donde el usuario ingrese un número natural y se muestre:
#si es par o no, si es primo o no, sus divisores y su factorial.
#Nota: importe y utilice el módulo operaciones_naturales.py.

import math

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def divisores(numero):
    for i in range(1, numero + 1):
            if numero % i == 0:
                print(i, end=" ")

def es_primo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True   

def factorial(numero): 
   return math.factorial(numero)