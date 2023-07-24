# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:03:36 2022

@author: Sabrina
"""

# En el archivo “clinica.txt” se encuentran almacenadas las visitas durante los tres últimos años a un centro de
# salud de la ciudad de Paraná, que posee varios consultorios: pediatría, ginecología, cardiología, etc., el
# archivo tiene 4 datos por línea separados por coma: código del servicio (número entero entre 1 y 15), nombre del
# servicio (string), fecha (dd/mm/aaaa), cantidad de visitas (número entero). Por razones de simplicidad se
# necesita dividir la información en un archivo por año: “clinica2020.txt”, “clinica2021.txt”, “clinica2022.txt”.
# Separe la información en un archivo por año. El archivo “clinica2022.txt” ya fue creado por lo que debe agregar
# la nueva información que se encuentra en “clinica.txt” sin perder los datos que contiene. Luego el usuario debe
# ingresar un año, el programa debe validar que el año ingresado es correcto (2020, 2021, 2022) y volver a dar la
# oportunidad de ingresarlo si es incorrecto. Para el año ingresado determine:  
# a- Cuáles fueron los tres servicios más requeridos durante todo el año
# b- El mes que más visitas tuvo 
# c- Cuántos pacientes visitaron la clínica en verano y cuántos en invierno
# d- Promedio de pacientes por día para el servicio de pediatría en julio 
# e- Cuáles fueron los dos servicios más requeridos en el verano  
# f- Cuántos pacientes visitaron la clínica en todo el año
import csv

with open ("clinica.txt", "r") as clinica, open("clinica2020.txt", "w") as c20, open("clinica2021.txt", "w") as c21, open("clinica2022.txt", "r+") as c22:
    lector=csv.reader(clinica, delimiter=',')
    c20=csv.writer(c20, delimiter=',')
    c21=csv.writer(c21, delimiter=',')
    c22=csv.writer(c22, delimiter=',')
    for linea in lector: #linea es una lista
        linea[3]= linea[3].rstrip('\n')
        fecha=linea[2].split('/')
        anio=int(fecha[2])
        if anio==2020:
            c20.writerow(linea)
        elif anio==2021:
            c21.writerow(linea)
        else:
            c22.writerow(linea)#le paso la lista de la linea
            
anio=int(input("Ingrese año:"))
# if anio!=2020 or anio!=2021 or anio!=2022:
#     anio=int(input("Ingrese otra vez el año: "))
        
datos=[[0]*15 for i in range (15)]#agrego otra columna para el codigo, la descripcion y el total    

if anio==2020:
    archivo="clinica2020.txt"
elif anio==2021:
    archivo="clinica2021.txt"
else:
    archivo="clinica2022.txt"
    
with open (archivo, "r") as archi:
    lector=csv.reader(archi, delimiter=',')
    for linea in lector:
        datos[int(linea[0])-1][0]=int(linea[0])#en el subindice 0 siempre se guarda el cero
        datos[int(linea[0])-1][1]=linea[1]
        fecha=linea[2].split('/')
        mes=int(fecha[1])
        datos[int(linea[0])-1][mes+1]+=int(linea[3])
