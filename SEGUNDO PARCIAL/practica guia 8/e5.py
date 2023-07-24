# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:27:38 2022

@author: Sabrina
"""

# Una empresa exportadora de granos vende sus productos a 10 países. Se dispone de una archivo export.txt
# con los datos de cada venta (exportación) durante el 2021. En cada línea hay tres datos correspondiente al
# código del país (entero entre 1 y 10) , la fecha de venta y el monto de la misma, donde la fecha es un 
# entero de 6 cifras (ddmmaa). Puede haber más de una venta en un mismo mes. Organice una lista de 10 filas (países) 
# x 12 columnas (meses) que contenga los montos de ventas exportados. Determinar e informar: 
#     a) El total exportado a cada país; 
#     b) ¿ A qué país corresponde el mayor monto exportado en marzo de 2021?. 
#     Utilice una función para calcular el ítem (b).

def mayor_monto_exportado(lista, mes):
    pais_mmonto=lista[0][mes-1]
    for i in range(len(lista)):
        if pais_mmonto<lista[i][mes-1]:
            pais_mmonto=lista[i][mes-1]
            pais=i
    return pais

ventas=[[0]*12 for i in range (10)]
with open ("export.txt", "r") as archivo:
    for linea in archivo:
        linea=linea.strip("\n")
        linea=linea.split(" ")
        pais=int(linea[0])
        mes=int(int(linea[1])/100)%100
        monto=int(linea[2])
        ventas[pais-1][mes-1]+=monto

for i in range(len(ventas)):
    print("el total exportado por cada pais fue de: ", sum(ventas[i]))
print("el pais de mayor monto exportado en marzo del 2021 fue el de codigo:", mayor_monto_exportado(ventas, 3)+1)