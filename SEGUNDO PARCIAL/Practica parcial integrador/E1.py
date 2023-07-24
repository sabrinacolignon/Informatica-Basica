# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:33:00 2022

@author: Sabrina
"""

# Una empresa distribuidora de equipos medicos vende articulos distintos y exporta a otros paises.
# Posee 8 sucursales y deses analizar el desempeño de las mismas en el año 2020.
# Para ello se dispone de un archivo de texto "ventas2020.csv" donde se encuentran almacenados
# en cada linea 3 datos (separados por comas) por cada operacion de venta realizada ese año:
# mes (1..12), sucursal(1..8), monto. Puede haber varias ventas en un mismo mes y sucursal.
# a- organice la matriz de 8 filas (sucursales) por 12 columnas (meses) y para cada celda acumule los montos vendidos.
# b- Determine la recaudacion anual de la sucursal 7.
# c- En el mes de mayo, cual fue la mayor recaudacion de una sucursal? Que sucursal lo logro?
# Use funciones.
import csv

def armado_matriz(matriz_ventas, archivo):
    lector=csv.reader(archivo, delimiter=',')
    for linea in lector:
        mes=int(linea[0])
        sucursal=int(linea[1])
        monto=float(linea[2])
        matriz_ventas[mes-1][sucursal-1]+=monto
    return matriz_ventas
    
def recaudacion_anual(lista, suc):
    recaudacion=0
    for i in range(len(lista)):
        recaudacion+=ventas[i][suc-1]#acumulo orque ouede haber nmas de un dato
    return recaudacion

def mayor_recaudacion(lista, mes):
    mayor_rec=lista[0]
    for i in range(len(lista)):
        if mayor_rec>lista[mes-1][i]:
            mayor_rec=lista[mes-1][i]
            suc_mayor_rec=i+1
    return mayor_rec, suc_mayor_rec         

ventas=[[0]*12 for i in range(8)]
archivo="ventas2020.csv"
with open (archivo, "r") as archivo:
    ventas=armado_matriz(ventas, archivo)
    
print("La recaudacion anual de la sucursal 7 es de: ", recaudacion_anual(ventas, 7))

print("La sucursal de mayor recaudacion y su monto en mayo fue: ", mayor_recaudacion(ventas, 4))
