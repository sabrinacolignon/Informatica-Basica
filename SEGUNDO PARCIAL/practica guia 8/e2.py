# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:46:06 2022

@author: Sabrina
"""

# Con la información obtenida en el ejercicio anterior escribir un archivo, correos.txt, con las direcciones
# de correo electrónico de los agentes. Este correo se forma con la primera letra del nombre seguido del
# apellido y el dominio "@ingenieria.edu.ar"

with open ("personal.txt", "r") as archivo:
    informacion=archivo.readlines()

mails=[]
listado=[]
nombre=[]
apellido=[]
for i in range(len(informacion)):
    listado.append(informacion[i].split(" "))
    nombre.append(listado[i][0])
    apellido.append(listado[i][1])
    mail=nombre[i][0]+apellido[i].rstrip('\n')+"@ingenieria.edu.ar"
    mails.append(mail.lower())

with open ("correos.txt", "w") as archivo_nuevo:
    archivo_nuevo.write(str(mails))