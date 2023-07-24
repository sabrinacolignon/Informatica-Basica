# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:29:42 2022

@author: Sabrina
"""

#Diseñe e implemente un programa en Python que calcule
#el Índice de masa corporal (IMC) de una persona a partir
#del peso y altura ingresados por un usuario. Informar la
#condición del usuario a partir de los valores obtenidos de
#IMC según la siguiente tabla:

peso=float(input("ingrese el peso de la persona: "))
altura=float(input("ingrese altura de la persona en metros: "))
imc=peso/(altura**2)
print("su imc es:", round(imc,1))

if imc<18.5:
    print("bajo peso.")
else:
    if 18.5<=imc<=24.9:
        print ("peso normal.")
    elif 25<imc<29.9:
        print("sobrepeso.")
    elif 30<imc<34.9:
        print("obesidad tipo 1.")
    elif 35<imc<39.9:
        print("obesidad tipo 2.")
    else:
        imc>=40
        print ("obesidad tipo 3.")
