# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:25:16 2022

@author: Sabrina
"""

#E10: Para determinar la condición final de los alumnos de un curso de la asignatura Química se ingresa
#el nombre del alumno, las dos notas de los parciales y la cantidad de trabajos prácticos aprobados.
#Escriba una función que determine la condición de cada alumno sabiendo que para regularizar la materia
#debe tener promedio de los parciales mayor a 60 y 5 o más trabajos prácticos aprobados, sino cumple con
#alguno de estos requisitos estará en condición de libre. Informe un listado con los nombres de los alumnos
#y su condición final (regular o libre).

def condicion(lista):
    condiciones=[]
    for i in range(len(lista)):
        prom=(lista[i][1]+lista[i][2])/2
        if prom>=60 and lista[i][3]>=5:
            condiciones.append([lista[i][0], "regular"])
        else:
            condiciones.append([lista[i][0], "libre"])
    return condiciones
            
lista=[]
nombre=input("ingrese nombre del alumno: ")
while nombre!=" ":
    nota1=int(input("ingrese primer nota del parcial: "))
    nota2=int(input("ingrese segunda nota del parcial: "))
    tp_ap=int(input("ingrese cantidad de trabajos aprobados: "))
    lista.append([nombre, nota1, nota2, tp_ap])
    nombre=input("ingrese nombre del alumno: ")

print("su condicion es: ", condicion(lista))