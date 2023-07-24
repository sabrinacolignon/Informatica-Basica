# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:09:17 2022

@author: Sabrina
"""

#Diseñe e implemente una función en Python para la creación de direcciones de e-mail institucionales.
#El usuario debe ingresar su nombre, apellido y el nombre de la empresa o institución a la que pertenece.
#Las direcciones de e-mail institucionales constan de: la primera letra del nombre del usuario, seguido
#de su apellido completo, seguido del @, seguido del nombre de la institución y por último un .com.
#Toda la dirección de e-mail debe estar en minúscula.
#Ejemplo: Nombre: Rodrigo
#               Apellido: Peralta
#               Institución: FIUNER
#               Dirección de e-mail institucional: rperalta@fiuner.com
def emails(nombre, apellido, institucion):
    email=nombre[0]+apellido+'@'+institucion+'.com'
    email_m=email.lower()
    return email_m

nombre=input("Ingrese nombre de la persona: ")
apellido=input("Ingrese apellido de la persona: ")
institucion=input("Ingrese institucion a la que la persona pertenece: ")
print("Su email institucional es: ", emails(nombre, apellido, institucion))