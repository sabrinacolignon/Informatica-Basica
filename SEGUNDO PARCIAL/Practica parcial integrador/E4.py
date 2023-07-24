# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:04:31 2022

@author: Sabrina
"""

# En un archivo de textos MATRICULA.CSV se disponen en cada linea los 12 datos de ingreso a 11 facultades de ingenieria
# en los últimos 10 años (10 lineas: 1er linea-2009, 2da linea-2010,...). En otro archivo de textos DESERCION.CSV se
# disponen los registros de deserción (número de estudiantes que abandonaron la carrera) de estas 11 facultades en los
# 10 últimos años. Determinar e informar mediante un programa:
# a) En qué año se produjo la mayor deserción sumando el número de abandono de todas las facultades; 
# b) El mayor % de abandono y la facultad donde se produjo en 2014;
# c) Cuantas facultades tuvieron una deserción superior a 50% en 2016.
# Utilice funciones.
import csv

def anio_max_desercion(lista):
    max_desercion=0
    total_desercion=[]
    for i in range(10):
        total_desercion.append(sum(lista[i]))
        if max_desercion<total_desercion[i]:
            max_desercion=total_desercion[i]
            anio=2009+i
    return anio

def porcentaje_abandono(matriz1, matriz2, anio):
    porcentaje_abandono=0
    for i in range(8):
        porcentaje=matriz1[2009-anio][i]/matriz2[2009-anio][i]*100
        if porcentaje>porcentaje_abandono:
            porcentaje_abandono=porcentaje
            facultad_max_abandono=i+1
    return porcentaje_abandono, facultad_max_abandono     

def calcula_desercion_superior(matriz1, matriz2, anio):   
    contador=0
    for i in range(8):
        porcentaje=matriz1[2009-anio][i]/matriz2[2009-anio][i]*100
        if porcentaje>50:
            contador+=1
    return contador
    
matriz_matricula=[]
with open("matricula.csv", "r") as archivo:
    lector=csv.reader(archivo, delimiter=",")
    for linea in lector:
        fila=[]
        for i in range(1,9):
            fila.append(int(linea[i]))
        matriz_matricula.append(fila)

matriz_desercion=[]
with open("desercion.csv", "r") as archivo:
    lector=csv.reader(archivo, delimiter=",")
    for linea in lector:
        fila=[]
        for i in range(1,9):
            fila.append(int(linea[i]))
        matriz_desercion.append(fila)

print("El año de mayor desercion fue:", anio_max_desercion(matriz_desercion))
print("El mayor % de abandono y la facultad donde se produjo en 2014 fueron: ",  porcentaje_abandono(matriz_desercion, 2014))
print("La cantidad de facultades quetuvieron una deserción superior a 50% en 2016 fue de: ", calcula_desercion_superior(matriz_desercion, 2016))