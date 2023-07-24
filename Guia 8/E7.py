# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:33:48 2022

@author: Sabrina
"""

# Diseñe e implemente en Pyhon las funcionalidades para obtener el Indice de masa corporal (IMC) de una persona
# y su condición de salud en base a este valor.
# Escriba un programa donde solicite al usuario: nombre, apellido, edad, dni, peso y altura, el cálculo de su
# IMC y su condición en base al IMC. Guarde en un archivo de texto todos los datos y resultados obtenidos.
# Evalúe el correcto funcionamiento del sistema cargando al menos 3 personas, siendo estas debidamente almacenadas.

def calcula_imc(lista):
    for i in range(len(lista)):
        imc=round(lista[i][3]/(lista[i][4]**2),1)
        if imc<18.5:
            condicion="bajo peso."
        elif 18.5<=imc<=24.9:
            condicion="peso normal."
        elif 25<imc<29.9:
            condicion="sobrepeso."
        elif 30<imc<34.9:
            condicion="obesidad tipo 1."
        elif 35<imc<39.9:
            condicion="obesidad tipo 2."
        else:
            condicion="obesidad tipo 3."
    return imc, condicion

datos_usuario=[]
continuar=1
while continuar==1:
    nombre=input("Ingrese nombre del usuario: ")
    apellido=input("Ingrese apellido del usuario: ")
    edad=int(input("Ingrese edad del usuario: "))
    peso=float(input("ingrese el peso del usuario: "))
    altura=float(input("ingrese altura del usuario en metros: "))
    datos_usuario.append([nombre, apellido, edad, peso, altura])
    continuar=int(input("desea ingresar una nueva persona? 1=SI, 2=NO "))

for i in range(len(datos_usuario)):
    imc, condicion=calcula_imc(datos_usuario)
    datos_usuario[i].append([imc, condicion])

with open ("datos_imc.txt", "w") as archivo:
    archivo.write(str(datos_usuario))