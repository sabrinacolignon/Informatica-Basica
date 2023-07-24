# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:44:51 2022

@author: Sabrina
"""

with open("informe.txt", "r+") as archivo:
    informe=archivo.readlines()
    informe=str(informe)
    contador=0
    nuevo_informe=[]
    if informe.replace("programa", "software"):
        contador+=1
        nuevo_informe=informe.replace("programa", "software")
    archivo.seek(0)
    archivo.write(str(nuevo_informe))
print("La palabra -programa- aparecio: ", contador, "veces.")