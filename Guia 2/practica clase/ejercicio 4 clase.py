# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:08:35 2022

@author: Sabrina
"""
#123
#213
#321
#132
#312
#231


numero1=int(input("ingrese numero 1: "))
numero2=int(input("ingrese numero 2: "))
numero3=int(input("ingrese numero 3: "))
if numero1<numero2>numero3:
    print("el mayor es el numero 1: ", numero1)#caso 3 y 5
elif numero3<numero1>numero2:
    print("el mayor numero es numero 2: ", numero2) #caso 4
elif numero1<numero3>numero2:
    print("el mayor numero es numero 3: ", numero3) #caso 1
else:
    print("los datos ingresados no son correctos.")
  
############ SEGUNDA FORMA ###############
#if a>b:
#    if a>c:
#        print(a)
#    else:
#        print (c)
#elif b>c:
#    print (b)
#else:
#   print (c)
#