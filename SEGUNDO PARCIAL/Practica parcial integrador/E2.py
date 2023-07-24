# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:02:32 2022

@author: Sabrina
"""
# 41698150,sabrina,colignon
# 41610786,adriel,irigoitia
# 45221895,sofia,rodriguez
# 56465455,felix,colignon
# 42156325,josefina,colignon
# 25684692,lorena,benitez
# Un archivo de textos LISTADO.TXT tiene una lista 3 datos por linea: dni, nombre y apellido de un agrupo de personas
# (una persona por línea), todos los nombres y apellidos se conforman de una sola palabra (no hay dobles apellidos, etc).
# Reescriba el archivo de forma que cada linea posea: DNI, Apellido. Nombre, email. Apellido y nombre deben tener inicial
# en mayúsculas y resto en minúsculas y la dirección de email debe formarse con la inicial del nombre+ apellidio+®+gmail.com

registros=[]
with open ("listado.txt", "r+") as archivo:
    for linea in archivo:
        linea=linea.rstrip('\n')
        linea=linea.split(",")
        dni=int(linea[0])
        nombre=linea[1]
        apellido=linea[2]
        registros.append([dni, nombre, apellido])
    for i in range(len(registros)):
        dni, nombre, apellido=registros[i]
        email=nombre[0]+apellido+"@gmail.com"
        email=email.lower()
        nombre=nombre.capitalize()
        apellido=apellido.capitalize()
        registros.append((dni, nombre, apellido, email))
    archivo.seek(0)
    archivo.write(str(registros))
        