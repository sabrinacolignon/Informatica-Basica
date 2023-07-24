# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:58:34 2022

@author: Sabrina
"""

nombres=[]
nombre=input("Ingrese nombre: ")
while nombre.lower() != "fin":
    nombres.append(nombre)
    nombre=input("Ingrese nombre: ")
nombres.sort()
print("La lista de nombres ordenados es: ", nombres)