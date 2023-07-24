# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:36:26 2022

@author: Sabrina
"""

#Diseñe e implemente una función que reciba como parámetro un número natural e indique todos sus divisores.
def divisores(numero):
    for i in range(1, numero + 1):
            if numero % i == 0:
                print(i, end=" ")

numero=int(input("ingrese un numero natural: "))
divisores(numero)