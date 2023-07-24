# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:58:39 2022

@author: Sabrina
"""

#calcule el área y el perímetro de un círculo cuyo radio se ingresa como dato.
#area del circulo: A=pi*radio*radio // P=2*pi*radio
import math
radio=float(input("ingrese el radio"))
area=math.pi*(radio**2)
perimetro=2*math.pi*radio
print("el area es: ", area)
print("el perimetro es: ", perimetro)