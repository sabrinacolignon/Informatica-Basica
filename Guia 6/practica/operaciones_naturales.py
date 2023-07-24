# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:17:36 2022

@author: Sabrina
"""

def es_par(numero):
    if numero%2==0:
        return True
    else:
        return False
    
def obtener_divisores(numero):
    divisores=[]
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_primo(numero):
    div=obtener_divisores(numero)
    if len(div)==2:
        return True
    else:
        return False
    
def factorial(numero):
    f=1
    for i in range(1, numero+1):
        f=f*i
    return f
#Factorial con recursividad (funcion que se llama a si misma):
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x*factorial(x-1))