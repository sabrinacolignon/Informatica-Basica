# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:51:41 2022

@author: Sabrina
"""

peso=float(input("ingrese peso en kg de la persona: "))
altura=float(input("ingrese altura en metros de la persona: "))
imc= peso/(altura*2)
print("el imc de la persona es: ", round(imc,2), "\n")

if imc<18.5:
    print("bajo peso.")
elif 18.5<=imc<24.9:
    print("peso normal.")
elif 25<imc<29.9:
    print("sobrepeso.")
elif 30<imc<34.9:
    print("obesidad tipo 1")
elif 35<imc<39.9:
    print("obesidad tipo 2")
elif imc>=40:
    print("obesidad tipo 3.")
else:
    print("los datos ingresados no estan en la tabla")