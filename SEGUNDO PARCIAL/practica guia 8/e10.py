# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:59:32 2022

@author: Sabrina
"""
# Lea el archivo de texto Lista.txt y obtenga el promedio de cada estudiante. Escriba otro archivo 
# Condicion.txt que contenga en la primera línea el nombre del alumno y su promedio y en la segunda línea
# la condición del alumno. La condición queda determinada según el promedio de las notas: entre 60 y 80,
# alumno regular, mayor a 80 promocional y libre en otro caso.
#Modifique el ejercicio anterior para que en lugar de escribir un nuevo archivo, se modifique Lista.txt
#añadiendo 2 filas más por alumno: una con el promedio y otra con la condición.

with open ("lista.txt", "r+") as archivo:
    datos=archivo.readlines()
    nombres=[]
    notas=[]
    for i in range(1, len(datos), 2):
        nombres.append(datos[i-1])
        notas.append(datos[i])
    promedio=[]
    for i in notas:
        n1, n2, n3=i.split(" ")
        prom=round((int(n1)+int(n2)+int(n3))/3,2)
        promedio.append(prom)
    
    archivo.seek(0)
    for i, a in enumerate(nombres):
        archivo.write(a.strip('\n'))
        archivo.write(f"-Promedio:{promedio[i]}\n")
        if promedio[i]>=80:
            condi="Promocional"
            archivo.write("Condición: "+condi+"\n")
        elif promedio[i]>=60:
            condi="Regular"
            archivo.write("Condición: "+condi+"\n")
        else: 
            condi="Libre"
            archivo.write("Condición: "+condi+"\n")