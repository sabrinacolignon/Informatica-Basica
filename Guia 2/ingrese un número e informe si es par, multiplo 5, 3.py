# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:55:49 2022

@author: Sabrina
"""

#Diseñe e implemente un programa en Python en donde se ingrese un número e informe:
#a) si es par o impar.
#b) si es múltiplo de 5.
#c) si es múltiplo de 3.
#d) si es múltiplo de 5 y 3 a la vez.

numero_ingresado=int(input("ingrese el numero con el que desea operar: "))
opcion=int(input("ingrese la opcion: 1(si es par o impar), 2(si es múltiplo de 5), 3(si es múltiplo de 3), 4 (si es múltiplo de 5 y 3 a la vez): "))
if opcion==1:
    if(numero_ingresado%2) == 0:
        print ("el numero es par")
    else:
        print ("el numero es impar")
elif opcion==2:
    if (numero_ingresado%5)==0:
        print ("el numero es multiplo de 5")
    else:
        print ("el numero no es multiplo de 5")
elif opcion==3:
    if (numero_ingresado%3)==0:
        print ("el numero es multiplo de 3")
    else:
        print ("el numero no es multiplo de 3")
elif opcion==4:
    if(numero_ingresado%5 and numero_ingresado%3)==0:
        print (" el numero múltiplo es de 5 y 3 a la vez")
    else:
        print("el numero no es multiplo de 5 y 3 a la vez")
else:
    print("la opcion ingresada no es correcta")