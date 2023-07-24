# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:59:51 2022

@author: Sabrina
"""

#Diseñe e implemente una función en Python para la creación de direcciones de e-mail institucionales.
#El usuario debe ingresar su nombre, apellido y el nombre de la empresa o institución a la que pertenece.
#Las direcciones de e-mail institucionales constan de: la primera letra del nombre del usuario,
#seguido de su apellido completo, seguido del @, seguido del nombre de la institución y por último un .com.
#Toda la dirección de e-mail debe estar en minúscula.
#Ejemplo: Nombre: Rodrigo
#Apellido: Peralta
#Institución: FIUNER
#Dirección de e-mail institucional: rperalta@fiuner.com

def emails(nombre, apellido, institucion):
    arroba='@'
    fin='.com'
    email=nombre[0]+apellido+arroba+institucion+fin
    email_m=email.lower()
    return email_m

nombre=input("ingrese nombre del usuario: ")
apellido=input("ingrese apellido del usuario: ")
institucion=input("ingrese institucion a la que pertenece el usuario: ")
email=emails(nombre, apellido, institucion)
print("Su email es: ", email)