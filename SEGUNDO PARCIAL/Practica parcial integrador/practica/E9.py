# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:51:37 2022

@author: Sabrina
"""

# Una empresa de Ingeniería Biomédica exporta a 8 países, además de las ventas locales. Se dispone de un archivo
# VENTAS2017.TXT que contiene en cada línea 4 números correspondiente a cada operación de venta realizada durante 2017:
# código Pais (1.8), monto de la venta, día (1..31), mes (1..12). Puede haber varias ventas en un mismo mes para un
# mismo país. Organice los montos de ventas de la empresa en una tabla o matriz de 8 filas x 12 columnas. Las primeras
# 12 columnas corresponden a cada mes de 2017. El programa debe obtener e informar:
    #a) el total vendido a cada país, indicando esta cifra en la columna 13 de la tabla; 
    #b) El mes de mayor monto de ventas de la empresa considerando(sumando) todos los países. 
import csv

def total_vendido_x_pais(lista):
    total_x_pais=[]
    for i in range(8):
        monto=sum(lista[i])
        total_x_pais.append(monto)
    return total_x_pais

def mes_mayor_monto_todos_paises(lista):
    mayor_monto=lista[0][0]
    for i in range(10):
        for j in range(12):
            if mayor_monto<lista[i][j]:
                mayor_monto=lista[i][j]
                mes_mayor_monto=j+1
    return mes_mayor_monto

ventas=[[0]*12 for i in range(8)]
with open("ventas.txt", "r") as archivo:
    lector=csv.reader(archivo, delimiter=",")
    for linea in lector:
        cod_pais=int(linea[0])
        monto_venta=float(linea[1])
        dia=int(linea[2])
        mes=int(linea[3])
        ventas[cod_pais-1][mes-1]+=monto_venta

total_vendido_x_pais(ventas) 
mes_mayor_monto_todos_paises(ventas)       