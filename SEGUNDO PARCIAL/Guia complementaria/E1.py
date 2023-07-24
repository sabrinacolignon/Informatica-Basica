# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:20:49 2022

@author: Sabrina
"""
#1. En una olimpíada estudiantil compiten N alumnos en 3 pruebas (1: matemáticas, 2: física y 3: computación).
#Se ingresan por cada inscripto el DNI y su número asignado para la competencia (entre 1 y N).
#Luego, sin orden alguno, se van ingresando ternas con los puntajes de cada prueba:
#nro de participante, código de actividad (1: matemáticas, 2: física y 3: computación), puntaje en la actividad.
#Escriba un algoritmo que determine:
#a) El DNI del ganador de la competencia y el puntaje total obtenido.
#b) El DNI del estudiante que ocupó el 2do lugar y su puntaje.
#c) ¿Qué puntaje obtuvo en Computación el ganador de la competencia?

terna_dni=[]
terna_cod=[]
terna_notas=[]

dni= int(input("ingrese dni del alumno: "))  
while dni!=0:
    cod= int(input("ingrese numero de participante: "))
    terna_dni.append(dni)
    terna_cod.append(cod)
    dni= int(input("ingrese dni del alumno: "))  

terna_notas=[[0]*3 for x in range (len(terna_dni))] #inicializo en cero

for i in range(len(terna_dni)*3):
    cod= int(input("ingrese numero de participante: "))
    materia=int(input("ingrese (1: matemáticas, 2: física y 3: computación): "))
    nota= int(input("ingrese nota del alumno: "))
    terna_notas[terna_cod.index(cod)][materia-1]=nota

print("el participante dni ", terna_dni[1], "con codigo: ", terna_cod[1], "tiene las siguentes notas: ")    
print(terna_notas[terna_cod.index(terna_cod[1])])#del codigo 1 el indice para acceder a las notas

max_pun= sum(terna_notas[0])
#seg_max=sum(terna_notas[0])
ganador=0
#segundo=0
for i in range (len(terna_dni)):
    if max_pun<sum(terna_notas[i]):
        seg_max=max_pun
        max_pun=sum(terna_notas[i])
        ganador=i
        segundo=i-1
        print("el ganador de la competencia es: ", terna_dni.index(i), "y su nota es: ", max_pun)
    elif segundo>sum(terna_notas[i]):
        seg_max=sum(terna_notas[i])
        print("el segundo ganador de la competencia es: ", terna_dni.index(i-1), "y su nota es: ", seg_max)


