# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:57:44 2022

@author: Sabrina
"""

#Dada una secuencia de ADN, escriba un programa para calcular el porcentaje de GC, es decir la cantidad
#porcentual de guaninas (G) y citosinas (C) que posee la secuencia.
#Secuencia de ADN: ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA
secuencia_adn="ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA"
suma_g=0
suma_c=0
for i in secuencia_adn:
    if i=='G':
        suma_g+=1
    elif i=='C':
        suma_c+=1
        
porcentaje_c=suma_c/len(secuencia_adn)
porcentaje_g=suma_g/len(secuencia_adn)
print("El porcentaje de g es de: ", porcentaje_g)
print("El porcentaje de c es de: ", porcentaje_c)