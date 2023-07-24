# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:36:59 2022

@author: Sabrina
"""

#Lea el archivo personal.txt que contiene un listado con los nombres  y apellidos de los
#agentes de la Facultad de Ingeniería de la UNER, y muestre el contenido del mismo por consola.

with open ("personal.txt", "r") as archivo:
    informacion=archivo.readlines()
print(informacion)