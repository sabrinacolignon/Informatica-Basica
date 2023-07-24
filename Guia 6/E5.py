# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:04:51 2022

@author: Sabrina
"""

#La serie de Fibonacci se calcula de la forma siguiente: 1 + 1 + 2 + 3 + 5 + 8 + 13 +...
#Donde cada término i se calcula sumando los 2 anteriores: ti=ti-1+ti-2, y los 2 términos iniciales valen 1.
#Escriba una función para calcular los primeros n números de la serie de Fibonacci y luego escriba un
#programa cliente que la utilice. 

def fibonacci(n):
   if n>1:
       return fibonacci(n-1) + fibonacci(n-2);  #función recursiva
   elif n==1:
       return 1
   else:
       return 0

numero=int(input("ingrese cantidad de numeros de la serie que se imprimiran: "))
print("la serie es: ")
print(fibonacci(numero))   