# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:35:42 2022

@author: Sabrina
"""

#Solicitar al usuario una lista de nombres de longitud indeterminada.
#El ingreso de nombres debe terminar cuando el usuario ingrese la palabra “fin”.
#Luego, mostrar los nombres ordenados alfabéticamente.

lista=[]
while True: #Ciclo infinito
    nombres= input("Escriba lista de nombres: ")
    lista.append(nombres)
    if nombres=="fin":
        break
lista.remove("fin")
print("la lista es: ", lista)
lista.sort()
print("La lista de los nombres ordenados alfabeticamente es: ")
print(lista)