# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:42:15 2022

@author: Sabrina
"""

#Leer N datos numéricos. Obtener la media (M) y la desviación estándar (DS) de la lista.

lista=[]
suma=0
n=int(input("ingrese cantidad de datos numericos: "))
for i in range (0,n):
    elementos=int(input("ingrese elementos a la lista: "))
    lista.append(elementos)
    suma+=elementos
media=suma/n
varianza = sum((l-media)**2 for l in lista) / (n-1) #uso compresion de lista
des_est = varianza**(1/2)

print("La lista numerica es: ", lista)
print("la media de los numeros es: ", media)
print("la varianza de los numeros es: ", varianza)
print("la desviacion estandar es: ", des_est)