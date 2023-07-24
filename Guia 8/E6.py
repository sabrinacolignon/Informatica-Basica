# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:27:50 2022

@author: Sabrina
"""

# Escriba un programa en Python que genere los n primeros números de la Serie de Fibonacci y
# los almacene en un archivo de texto. Los n primeros números y el nombre del archivo son indicados por el
# usuario a través de la consola.

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

numeros=int(input("Ingrese los n primeros numeros de la serie: "))
nombre_archivo=input("ingrese nombre del archivo fisico: ")

with open(nombre_archivo, "w") as archi:
    archi.write(str(fib(numeros)))