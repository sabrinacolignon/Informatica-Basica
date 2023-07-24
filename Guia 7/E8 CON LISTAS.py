# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:16:57 2022

@author: Sabrina
"""

def crea_emails(lista):
    n_email=[]
    for i in range(len(lista)):
        nombre,apellido,institucion=lista[i]
        email=nombre[0]+apellido+'@'+institucion+'.com'
        n_email.append(email.lower())
    return n_email

lista=[]
continuar=1
while continuar==1:
    nombre=input("Ingrese nombre del usuario: ")
    apellido=input("Ingrese apellido del usuario: ")
    institucion=input("Ingrese institucion a la que pertenece el usuario: ")
    lista.append((nombre, apellido, institucion))
    continuar=int(input("desea ingresar una nueva persona? 1=SI, 2=NO "))

print("El email institucional de los usuarios es: ", crea_emails(lista))
