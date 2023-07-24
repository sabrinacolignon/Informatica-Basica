# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:08:26 2022

@author: Sabrina
"""

numeros=int(input("ingrese numeros naturales: "))
suma=0
while numeros>0:
    suma+=numeros
    salida=int(input("ingrese -1 si desea salir del ciclo: "))
    if salida==-1:
        print("-----SALIDA DEL CICLO-----")
        break
print("la suma de los numeros naturales es: ", suma)

#OTRA FORMA:
#x=int(input("ingrese"))
#suma=0
#while not x==-1:
    #suma+=x
    #x=int(input("otra vez"))
#print(suma)
