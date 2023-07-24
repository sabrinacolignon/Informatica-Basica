# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:03:38 2022

@author: Sabrina
"""

lista=[]
nombre=input("ingrese nombre: ")
nota1=int(input("ingrese nota 1: "))
nota2=int(input("ingrese nota 2: "))
lista.append(nombre)
lista.append(nota1)
lista.append(nota2)
print("Nombre del alumno:")
print(lista[0])
promedio=(lista[1]+lista[2])//2
print("Promedio de sus dos notas:")
print(promedio)