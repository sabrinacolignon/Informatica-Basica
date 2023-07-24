# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:53:26 2022

@author: Sabrina
"""

import random as r
numero=r.randint(1,100)
contador=0
for i in range(1,101): #va entre 1 y 100
    ciclo=range(1, numero+1)
    div_exactas=0
    for i in ciclo: #va cambiando entre los numeros para ver todos los dividores del mismo numero
        if numero/i==0:
            div_exactas+=1
        if div_exactas==2:
            print("el numero ", numero,"es primo")
        else:
            print("el numero ", numero,"no es primo")
