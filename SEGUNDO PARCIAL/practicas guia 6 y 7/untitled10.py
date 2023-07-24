# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:03:37 2022

@author: Sabrina
"""

#Solicitar al usuario una lista de nombres de longitud indeterminada.
#El ingreso de nombres debe terminar cuando el usuario ingrese la palabra “fin”.
#Luego, mostrar los nombres ordenados alfabéticamente.

nombre=input("Ingrese nombres: ")
nombres=[]
while nombre!="fin":
    nombres.append(nombre)
    nombre=input("Ingrese nombres: ")

nombres.sort()
print("La lista de nombres es: ")
print(nombres)