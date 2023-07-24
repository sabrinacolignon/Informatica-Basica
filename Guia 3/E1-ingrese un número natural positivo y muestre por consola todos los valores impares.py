# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:56:52 2022

@author: Sabrina
"""

numero=int(input("ingrese numero natural: "))
for i in range (1, numero+1):
    if (i%2!=0):
        print("los numeros impares son: ", i)
    
#CON WHILE:
#c=0
#i=-1
#while c<x:
    #i=i+1
    #c=2*i+1
    #if(c<=x):#manejo lo que voy a imprimir
        #print(c)