# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:48:45 2022

@author: Sabrina
"""

# Lea el archivo de texto Lista.txt y obtenga el promedio de cada estudiante. Escriba otro archivo Condicion.txt que
# contenga en la primera línea el nombre del alumno y su promedio y en la segunda línea la condición del alumno.
# La condición queda determinada según el promedio de las notas: entre 60 y 80, alumno regular, mayor a 80 promocional
# y libre en otro caso.

lista_nombres=[]
lista_notas=[]
with open ("lista.txt", "r") as archivo:
    datos=archivo.readlines()
for i in range(1, len(datos), 2):
    lista_nombres.append(datos[i-1])
    lista_notas.append(datos[i])
promedio=[]
for nota in lista_notas:
    n1, n2, n3=nota.split()
    p=(int(n1)+int(n2)+int(n3))//3
    promedio.append(p)
for i,a in enumerate(lista_nombres):
    print(a, end='')
    print("promedio: ", promedio[i])

with open ("condicion.txt", "w") as archivo:
    for i,a in enumerate(lista_nombres):
        archivo.write(a.strip('\n'))
        archivo.write(f". Promedio:{promedio[i]}\n")
        if promedio[i]>=80:
            condicion="promocional"
        elif promedio[i]>=60:
            condicion="regular"
        else:
            condicion="libre"
        archivo.write("Condicion: "+condicion+'\n')
        
        