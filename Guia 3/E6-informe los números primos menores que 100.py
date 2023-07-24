# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:36:27 2022

@author: Sabrina
"""
#import random as r
#Escriba un programa en Python que informe los números primos menores que 100.
numero=1
while numero<=100:
    contador=1
    div_exactas=0
    while contador<=numero:
        if numero%contador==0:#si el resto de la division es cero entonces
            div_exactas+=1#contabilizo las divisiones exactas
        contador+=1
    if div_exactas==2:
        print("el numero: ", numero, "es primo.")
    
    numero+=1 #contabiliza de 1 a 100
     