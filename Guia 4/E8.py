# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:12:56 2022

@author: Sabrina
"""

#Leer el dni y las calificaciones (una calificación por alumno) de un grupo de alumnos que asistieron 
#a y almacenarlos en una lista. Los datos finalizan con el dni 0. Se desea obtener como información de salida:
#a. Un listado de los DNI de los alumnos aprobados.
#b. Las 2 mayores calificaciones y los DNI de los alumnos que las obtuvieron.
2
lista=[]
aprobados=[]
cantidad_aprob=0
dni=int(input("ingrese dni del alumno: "))
while dni!=0:
    nota=int(input("ingrese nota del alumno: "))
    lista.append([dni, nota])
    dni=int(input("ingrese dni del alumno: "))

for i in lista:
    if i[1]>=60:
        aprobados= aprobados + [i[0]]
        cantidad_aprob+=1
print("la cantidad de alumnos que aprobaron son :", cantidad_aprob)
print("los alumnos aprobados son: ", aprobados)

mayor1=[0,0]#[0,-1]
mayor2=[0,0]#[0,-1]

for i in lista:
    if i[1]>mayor1[1]:
        mayor2=mayor1
        mayor1=i
    elif i[1]>mayor2[1]:
        mayor2=i
print("el primer mayor es: ", mayor1)
print("el segundo mayor es: ", mayor2)

    