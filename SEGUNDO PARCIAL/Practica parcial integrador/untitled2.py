# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:47:16 2022

@author: Sabrina
"""

def inserta_palabra(c1, c2, indice):
    sep_c1=c1.split(" ")
    sep_c1.insert(indice, c2)
    c_final=" ".join(sep_c1)
    return c_final

c1="hola como estas"
c2="vas"
indice=2
print(inserta_palabra(c1, c2, indice))