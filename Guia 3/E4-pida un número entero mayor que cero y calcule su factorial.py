# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:19:41 2022

@author: Sabrina
"""

#Escriba un programa que pida un número entero mayor que cero y calcule su factorial.
numero=int(input("ingrese numero entero: "))
factorial=1
if numero>0:
    for i in range(1, numero+1):
        factorial*=i
print("el factorial del numero es: ", factorial)