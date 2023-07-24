# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:16:40 2022

@author: Sabrina
"""

#Ingresar un valor numérico correspondiente a una medida en pies y
#devolver la cantidad equivalente en metros. Nota: 1 pie = 0,3048 metros.

medida_ingresada= float (input("ingrese medida en pies: "))
conversion= medida_ingresada*0.3048
print ("la conversion en metros es: ", conversion)