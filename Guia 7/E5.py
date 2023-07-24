# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:22:03 2022

@author: Sabrina
"""

#Escribir un programa en Python que pregunte por una muestra de números, separados por comas,
#los guarde en una lista y muestre por pantalla su media y desvío.

cadena_n=input("Introduzca una muestra de números separados por comas: ")
cadena_n=cadena_n.split(',')

for i in range(len(cadena_n)):
    cadena_n[i]=int(cadena_n[i])

cadena_n=tuple(cadena_n)
acum=0
acum_desv=0
for i in cadena_n:
    acum+=i
    acum_desv+=i**2
    
media=acum/len(cadena_n)
desvio_s=(acum_desv/len(cadena_n)-media**2)**(1/2)

print('La media es', media, ', y la desviación típica es', desvio_s)