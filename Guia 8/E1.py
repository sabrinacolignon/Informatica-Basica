# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:33:04 2022

@author: Sabrina
"""
#Lea el archivo personal.txt que contiene un listado con los nombres  y apellidos de los agentes
#de la Facultad de Ingeniería de la UNER, y muestre el contenido del mismo por consola.
archi=open ("personal.txt")
info=archi.read()
print(info)