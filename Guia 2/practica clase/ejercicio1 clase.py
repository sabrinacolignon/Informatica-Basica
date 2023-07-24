# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:58:39 2022

@author: Sabrina
"""

numero=int(input("ingrese numero para trabajar: "))
if numero%2==0:
    print("el numero: ", numero, "es par.")
else:
    print("el numero ingresado es impar.")
if numero%5==0:
    print("el numero: ", numero, "es multiplo de 5.")
    div5=True
else:
    print("el numero no es multiplo por 5.")
    div5=False
if numero%3==0:
    print("el numero: ", numero, "es multiplo de 3")
    div3=True
else:
    print("el numero no es multiplo de 3.")
    div3=False
if div5 and div3: #utilizo dos variables boolenanas->mas eficiente
    print("el numero: ", numero,"es multiplo de 5 y 3 a la vez.")
else:
    print("el numero no es multiplo de 5 y 3 a la vez.")
    