# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:09:17 2022

@author: Sabrina
"""

#Para determinar la condición final de los alumnos de un curso de la asignatura Química se ingresa
#el nombre del alumno, las dos notas de los parciales y la cantidad de trabajos prácticos aprobados.
#Escriba una función que determine la condición de cada alumno sabiendo que para regularizar la materia
#debe tener promedio de los parciales mayor a 60 y 5 o más trabajos prácticos aprobados, sino cumple con
#alguno de estos requisitos estará en condición de libre. Informe un listado con los nombres
#de los alumnos y su condición final (regular o libre).

def condicion(lista):
    aprobados=[]
    for i in range(len(lista)):
        promedio_parciales=(lista[i][2]+lista[i][2])/2
        if promedio_parciales>=60 and lista [i][3]>=5:
            aprobados.append([lista[i][0], "regular"])
        else:
            aprobados.append([lista[i][0], "libre"])
    return aprobados

alumnos=[]
nombre=input("Ingrese nombre del alumno: ")
while nombre!=' ':
    n_parcial1=int(input("Ingrese nota del primer parcial: "))
    n_parcial2=int(input("Ingrese nota del segundo parcial: "))
    tp_ap=int(input("Ingrese cantidad de trabajos aprobados: "))
    alumnos.append([nombre, n_parcial1, n_parcial2, tp_ap])
    nombre=input("Ingrese nombre del alumno:")

print("La condicion de los alumnos es: ")
print(condicion(alumnos))