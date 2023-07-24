# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:56:49 2022

@author: Sabrina
"""

#Escriba un programa que pregunte cuántos números se van a introducir, pida esos
#números e informe el mayor, el menor y la media.

numeros_intro=int(input("ingrese cuantos numeros va a introducir: "))
aux=0
maximo=0
suma=0
for numeros_intro in range(1, numeros_intro+1):
    numero=int(input("ingrese numero: "))
    minimo=numero
    if numero<minimo:
        minimo=numero 
    if numero>maximo:
        maximo=numero
    aux+=numero
    media= aux/numeros_intro
print("el numero minimo es: ", minimo)
print("el numero maximo es: ", maximo)
print("la media de los numeros es: ", media)
    
    
    