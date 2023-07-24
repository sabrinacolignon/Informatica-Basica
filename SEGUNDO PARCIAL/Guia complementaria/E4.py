# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:32:14 2022

@author: Sabrina
"""
#4. Se ingresan por pantalla los informes diarios de casos reportados de infectados por COVID19 durante
#los meses de marzo a noviembre inclusive en los 16 departamentos de una provincia. 
#Se ingresan los datos de la siguiente manera: día, mes, cantidad de casos reportados.
#Escriba un programa que organice una matriz de 16 filas (departamentos) por 9 columnas (meses) y obtenga e informe: 
#a) El % de casos registrados en el depto 5 del mes de mayo, respecto de todos los casos que se registraron en
    #ese mes en la provincia.
#b) La menor cantidad de casos registrada en julio y en qué depto ocurrió. 
#c) Qué % de aumento de casos se dio en el depto 11 en junio respecto de mayo?
fila=16
columna=9
casos=[]
for i in range (fila):
    for j in range (columna):
        departamento=int(input("ingrese numero de departamento: "))
        dia=int(input("ingrese dia del caso reportado: "))
        meses=int(input("ingrese mes del caso reportado: "))
        casos_reportados=int(input("ingrese cantidad de casos del dia: "))
        casos[departamento-1][meses-1]=casos_reportados

casos_mayo=0
for i in columna:
    casos_mayo+=casos[i][2]
porcentaje=round((casos[4][2]/casos_mayo)*100,2)
print("El % de casos registrados en el depto 5 del mes de mayo, respecto de todos los casos que se registraron en ese mes en la provincia")
print("es de:", casos_mayo, "%")

menor_cant_casos=sum(casos[0][6])
departamento=0
for i in range(fila):
    if menor_cant_casos<sum(casos[i][4]):
       menor_cant_casos=sum(casos[i][4])
       departamento=i+1
       print("La menor cantidad de casos en julio, ocurrio en el departamento: ", departamento)
       
porc_junio=round(((casos[10][3]-(casos[10][2]))/(casos[10][2])*100,2))
if porc_junio>0:
    print('c) en el dpto 11 el porcentaje de aumento entre mayo-junio fue de:',porc_junio,'%')
else:
    print('c) no hubo porcentaje de aumento entre mayo-junio en el dpto 11, sino un declive del',porc_junio,'% de casos con respecto a mayo')