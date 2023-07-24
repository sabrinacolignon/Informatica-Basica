# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:27:40 2022

@author: Sabrina
"""
#Diseñe e implemente un programa en Python que lea un número entero e informe si
#es primo o no.
numero=int(input("ingrese numero entero: "))
control=1
div_exactas=0
while control<=numero:
    if numero % control==0: #si es =0 la division es exacta
        div_exactas+=1    
    control+=1
if div_exactas==2:
    print("el numero", numero, "es primo")
else:
    print("el numero", numero, "no es primo")
    
#OTRA FORMA:
#GENERO NUMERO AL AZAR EN VEZ DE INGRESARLO: 
#import random as r
#numero=r.randint(0,20)
#for i in range(1, numero+1) // podria arrancar el rango en 2 e ir hasta numero/2
    #if numero%i==0:
        #div+=1 //cuento la cantidad de divisiones exactas
    #if div==2:
        #print("es primo")
    #else:
        #print("no es primo")
    
