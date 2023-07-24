# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:59:48 2022

@author: Sabrina
"""
#Exhibir en pantalla 50 datos numéricos generados al azar entre 1 y 5000. Obtener
#como salida los siguientes parámetros estadísticos:
#a) la media
#b) los 2 mayores
#c) el menor de la lista.

import random
aux=0

suma=0
for i in range(5):
    numero=random.randint(1, 5000)
    print("El numero generado es: ", numero)
    suma+=numero
    media=suma/5
    if i==0:
        menor=numero
        mayor1=numero
        mayor2=numero
    else:
        if numero>mayor1:
            mayor2=mayor1
            mayor1=numero
        elif numero>mayor2:
            mayor2=numero
        if numero<menor:
            menor=numero

print("La media de los numeros es: ", media)
print("El primer mayor es: ", mayor1," y el segundo mayor es: ", mayor2)
print("El menor de la lista es: ", menor)



