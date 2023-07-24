# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:03:13 2022

@author: Sabrina
"""

# Escriba un programa que lea las temperaturas máximas diarias obtenidas en una región, a lo largo de un período
# de casi un año. Estas temperaturas están almacenadas en un archivo de texto TEMP.CSV (separados por comas); con un
# dato por linea. Entre los valores registrados en la secuencia se hallan algunos datos ficticios expresados con 999.9,
# lo cual significa que por problemas en el sensor no se pudo obtener la temperatura máxima de ese día.
# El programa debe realizar lo siguiente:
# a) Lea los datos de las temperaturas y organicelos en una lista.
# b) A través de una función, reemplace los valores 999.9 por el promedio entre el registro anterior y el posterior,
# no hay faltantes consecutivos. Si el 999.9 está en un extremo reemplazarlo con el dato más cercano

def reemplaza_faltantes(lista):
    for i in range(len(lista)):
        if lista[i]==999.9:
            lista[i]=round((lista[i-1]+lista[i+1])/2,1)
        elif lista[0]==999.9:
            lista[0]=lista[1]
        elif lista[-1]==999.9:
            lista[-1]=lista[-2]
    return lista

lista=[]
with open("temp.csv.txt", "r") as archivo:
    todo=archivo.readlines()
    for linea in todo:
        linea=linea.rstrip("\n")
        temp=float(linea)
        lista.append(temp)        
    
reemplaza_faltantes(lista)


