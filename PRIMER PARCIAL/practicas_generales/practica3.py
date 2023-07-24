# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:52:59 2022

@author: Sabrina
"""

sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo: "))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Lista ordenada")
print(sueldos)