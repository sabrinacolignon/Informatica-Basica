# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:06:18 2022

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
#import random as r

def gasto_anual_x_fac(lista):
    gasto_anual=[]
    for i in range(10):
        gasto_a=sum(lista[i])
        gasto_anual.append(gasto_a)
    return gasto_anual

def gasto_superior_4M(lista):
    contador=0
    for i in lista:
        acumulador=sum(i)
        if acumulador>4000000:
            contador+=1
    return contador

def menor_gasto_mensual(lista):
    menor_monto=lista[0][0]
    for i in range(12):
        for j in range(10):
            if menor_monto>lista[i][j]:
                menor_monto=lista[i][j]
                facultad_menor_monto=j+1
    return facultad_menor_monto, menor_monto

gastos_facultad=[[0]*12 for i in range(10)]
with open ("gastos.csv", "r") as archivo:
    lector=csv.reader(archivo, delimiter=",")
    for linea in lector:
        cod_fac=int(linea[0])
        mes=int(linea[1])
        monto=float(linea[2])
        gastos_facultad[cod_fac-1][mes-1]+=monto

print(gasto_anual_x_fac(gastos_facultad))
print(gasto_superior_4M(gastos_facultad))
print(menor_gasto_mensual(gastos_facultad))

# gastos_facultad=[]
# for i in range(12):
#     fila=[]
#     for j in range(10):
#         fila.append(r.randint(10000,10000000))
#     gastos_facultad.append(fila)



        