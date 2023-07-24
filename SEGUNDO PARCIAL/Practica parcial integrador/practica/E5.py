# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:19:37 2022

@author: Sabrina
"""

# Una empresa exportadora de granos vende sus productos a 10 países. Se dispone de una archivo export.txt con los datos
# de cada venta (exportación) durante el 2021. En cada línea hay tres datos correspondiente al código del país
# (entero entre 1 y 10) , la fecha de venta y el monto de la misma, donde la fecha es un entero de 6 cifras (ddmmaa).
# Puede haber más de una venta en un mismo mes. Organice una lista de 10 filas (países) x 12 columnas (meses) que contenga
# los montos de ventas exportados. Determinar e informar: a) El total exportado a cada país; b) ¿ A qué país corresponde el
# mayor monto exportado en marzo de 2021?. Utilice una función para calcular el ítem (b).

def total_exportado(lista):
    total_pais=[]
    for i in range(len(lista)):
        total=sum(lista[i])
        total_pais.append(total)
    return total_pais

def max_monto(lista, mes):
    maximo=lista[0][mes-1]
    for i in range(len(lista)):
        if maximo<lista[i][mes-1]:
            maximo=lista[i][mes-1]
            pais_maximo=i+1
    return pais_maximo
    
ventas=[[0]*12 for i in range(10)]
with open("export.txt", "r") as archivo:
    for linea in archivo:
        linea=linea.rstrip('\n')
        linea=linea.split(' ')
        cod_pais=int(linea[0])
        mes=int(int(linea[1])/100)%100
        monto=float(linea[2])
        ventas[cod_pais-1][mes-1]+=monto