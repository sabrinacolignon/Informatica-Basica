# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:49:55 2022

@author: Sabrina
"""

#soluciones o raíces de una ecuación cuadrática del tipo ax2+bx+c=0
#a=4, b=12, c=9

a= int(input("ingrese el coeficiente a: "))
b= int(input("ingrese el coeficiente b: "))
c= int(input("ingrese el coeficiente c: "))

discriminante= (b**2)-(4*a*c)

raiz1= (-b-(discriminante**0.5))/(2*a)
raiz2= (-b+(discriminante**0.5))/(2*a)

print("la primer raiz es: ", raiz1)
print("la segunda raiz es: ", raiz2)