# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:51:59 2022

@author: Sabrina
"""

# Un archivo de textos LISTADO.TXT tiene una lista 3 datos por linea: dni, nombre y apellido de un agrupo de personas
# (una persona por línea), todos los nombres y apellidos se conforman de una sola palabra (no hay dobles apellidos, etc).
# Reescriba el archivo de forma que cada linea posea: DNI, Apellido. Nombre, email. Apellido y nombre deben tener inicial
# en mayúsculas y resto en minúsculas y la dirección de email debe formarse con la inicial del nombre+ apellidio+®+gmail.com

lista=[]
lista_escribir=[]
with open ("listado.txt", "r+") as archivo:
    datos=archivo.readlines()
    for linea in datos:
        linea=linea.rstrip('\n')
        linea=linea.split(',')
        dni=linea[0]
        nombre=linea[1]
        apellido=linea[2]
        lista.append((dni, nombre, apellido))
    for i in range(len(lista)):
        dni, nombre, apellido=lista[i]
        email=nombre[0]+apellido+"@gmail.com"
        email=email.lower()
        nombre=nombre.capitalize()
        apellido=apellido.capitalize()
        lista_escribir.append((dni, nombre, apellido, email))
    archivo.seek(0)
    archivo.write(str(lista_escribir))