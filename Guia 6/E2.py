# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:43:14 2022

@author: Sabrina
"""

#Diseñe e implemente una función que reciba como parámetro un número natural e indique:
#True si es un número primo y False si no lo es. Compruebe su correcto funcionamiento
#con dos valores ingresados por el usuario.

def primo_o_no(numero):
    div=0
    for i in range(1, numero+1):
        if numero%i==0:
            div+=1
        if div==2:
            return True
        else:
            return False

numero=int(input("ingrese numero natural: "))
print("si el numero ingresado es primo saldra true, en caso contrario false: ")
print(primo_o_no(numero))