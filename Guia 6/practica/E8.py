# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:03:39 2022

@author: Sabrina
"""

#Construya el módulo operaciones_naturales.py, este debe contener las funciones: es_par(numero), divisores(numero),
#es_primo(numero) y factorial(numero), diseñadas e implementadas en los ejercicios previos y ejemplos.
#Diseñe e implemente un programa en Python donde el usuario ingrese un número natural y se muestre:
#si es par o no, si es primo o no, sus divisores y su factorial. Nota: importe y utilice el
#módulo operaciones_naturales.py.

import operaciones_naturales

numero=int(input("ingrese numero para realizar las operaciones: "))
print("Si el numero es par saldrá True, en caso contrario False: ", operaciones_naturales.es_par(numero))
print("Si el numero es primo saldrá True, en caso contrario False: ", operaciones_naturales.es_primo(numero))
print("Los divisores de ", numero,"son: ", operaciones_naturales.obtener_divisores(numero))
print("El factorial de ", numero,"! es: ", operaciones_naturales.factorial(numero))
