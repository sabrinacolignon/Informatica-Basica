# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:57:24 2022

@author: Sabrina
"""

#Diseñe e implemente una función en Python que multiplique una cantidad variable
#de números ingresados por el usuario y devuelva el resultado.
import random as r

def multiplicacion(numero):
    producto=1
    for n in numero:
        producto*=n
    return producto

lista=[]
corte=int(input("ingrese cantidad de numeros que desea ingresar: "))
for i in range(corte):
    numero=int(input("ingrese numeros: "))
    lista.append(numero)
    
print("la cantidad de elementos es: ", len(lista))
print("su producto es: ", multiplicacion(lista))