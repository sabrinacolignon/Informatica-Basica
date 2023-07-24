# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:34:16 2022

@author: Sabrina
"""

# Lea el archivo personal.txt que contiene un listado con los nombres  y apellidos de los agentes de la Facultad de Ingeniería
# de la UNER, y muestre el contenido del mismo por consola.
# Con la información obtenida en el ejercicio anterior escribir un archivo, correos.txt, con las direcciones de correo
# electrónico de los agentes. Este correo se forma con la primera letra del nombre seguido del apellido y el dominio
# "@ingenieria.edu.ar"

def crea_emails(lista):
    emails=[]
    for i in range(len(lista)):
        nombre,apellido=lista[i]
        email=nombre[0]+apellido+"@ingenieria.edu.ar"
        email=email.lower()
        emails.append(email)
    return emails
        
    
datos_persona=[]    
with open ("personal.txt", "r") as archivo:
    for linea in archivo:
        linea=linea.rstrip('\n')
        linea=linea.split(' ')
        nombre=linea[0]
        apellido=linea[1]
        datos_persona.append((nombre, apellido))

lista_emails=crea_emails(datos_persona)

with open("correos.txt", "w") as archivo:
    archivo.write(str(lista_emails))
        
        