# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:16:19 2022

@author: Sabrina
"""

# Una universidad tiene 10 facultades. Escriba un programa que acceda al archivo GASTOS.CSV desde el cual se deben leer
# los datos de compras o gastos realizados por cada facultad en el 2021 (tres datos por línea separados por coma):
# cod. facultad (de a 1 a 10), mes, (de 1 a 12) y monto. El programa debe organizar una matriz de 10 filas (facultades)
# por 12 columnas (meses) donde cada elemento de la matriz guarda el total gastado en ese mes por una Facultad.
# Nota: en un mismo mes, una misma Facultad puede realizar varios gastos. Determinar:
# a) el gasto final anual de cada facultad;
# b) Cuántas facultades gastaron más de 4 millones de pesos;
# c) La facultad y el monto correspondiente al menor gasto mensual de toda la tabla.
# Completar los ítems a, b y c usando funciones.
import csv

def gasto_final_anual(lista):
    gasto_anual=[]
    for i in range(len(lista)):
        gasto=sum(lista[i])
        gasto_anual.append(gasto)
    return gasto_anual

def gasto_superior(lista):
    contador=0
    for i in lista:
        acumulador=sum(i)
        if acumulador>4000000:
            contador+=1
    return contador

def menor_gasto_mensual(lista):
    menor_gasto=lista[0][0]
    for i in range(10):
        for j in range(12):
            if menor_gasto>lista[i][j]:
                menor_gasto=lista[i][j]
                fac_menor=i+1
    return menor_gasto, fac_menor
    
gastos=[[0]*12 for i in range(10)]
with open("castos.csv", "r") as archivo:
    lector=csv.reader(archivo, delimiter=',')
    for linea in lector:
        cod_fac=int(linea[0])
        mes=int(linea[1])
        monto=float(linea[2])
        gastos[cod_fac-1][mes-1]+=monto