# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:31:48 2022

@author: Sabrina
"""

lista_n=input("Introducza los numeros de la lista: ")
#lista_n=lista_n.split(',')

# for i in range(len(lista_n)):
#     lista_n[i]=int(lista_n[i])
n=list(map(int, lista_n.split(',')))
print(sum(n)/len(lista_n))
# suma=0
# for i in lista_n:
#     suma+=i
#media=suma/len(lista_n)
#print("La media es: ", round(media,2))


