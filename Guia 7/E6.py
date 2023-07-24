# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:30:09 2022

@author: Sabrina
"""

#Dada una secuencia de ADN, escriba un programa para calcular el porcentaje de GC,
#es decir la cantidad porcentual de guaninas (G) y citosinas (C) que posee la secuencia.
#Secuencia de ADN: ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA

sec_adn="ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA"

contador_c=0
contador_g=0
for i in sec_adn:
    if 'C'==i:
        contador_c+=1
    elif 'G'==i:
        contador_g+=1


porcentaje_c=(contador_c/len(sec_adn))*100
porcentaje_g=(contador_g/len(sec_adn))*100
print("El porcentaje de citocinas en la secuencia de adn es de: ", porcentaje_c)
print("El porcentaje de guaninas en la secuencia de adn es de: ", porcentaje_g)