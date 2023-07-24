# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:36:54 2022

@author: Sabrina
"""

#Escriba un programa en Python donde el usuario ingrese números naturales, se
#sumen y se muestre el resultado por pantalla. Para que el usuario deje de añadir
#números a la suma debe ingresar el valor -1
numero_ingresado=int(input("ingrese numeros naturales: "))
suma=0
while numero_ingresado>0:
    suma+=numero_ingresado 
    salida=int(input("si desea salir del ciclo ingrese -1, sino ingrese otro numero natural: \n"))
    if salida==-1:
        print("salida del ciclo")
        break
print("la suma de los numeros ingresados es: ", suma)