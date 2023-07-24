# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:51:36 2022

@author: Sabrina
"""

#Escriba una función para calcular el mínimo común múltiplo (m.c.m.) de dos números enteros dados.
def mcm(numero1, numero2):
    z=max(numero1, numero2)
    while True:
        if (z% numero1==0) and (z%numero2==0):
            return z
        z+=1

numero1=int(input("ingrese primer numero para calcular mcm: "))
numero2=int(input("ingrese segundo numero para calcular mcm: "))
print("el mcm es: ", mcm(numero1, numero2))