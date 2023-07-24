# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:10:33 2022

@author: Sabrina
"""

#Escriba un programa en Python donde se ingrese tres números e informe el mayor
numero1=int(input("ingrese primer numero: "))
numero2=int(input("ingrese segundo numero: "))
numero3=int(input("ingrese tercer numero: "))

if numero1<numero2>numero3:
    print("el mayor numero es: ", numero1)
elif numero2<numero1>numero3:
    print("el mayor numero es: ", numero2)
else:
    numero1<numero3>numero2
    print("el mayor numero es: ", numero3)
