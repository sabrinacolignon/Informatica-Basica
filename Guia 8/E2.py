# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:37:19 2022

@author: Sabrina
"""

#Con la información obtenida en el ejercicio anterior escribir un archivo, correos.txt, con las direcciones
#de correo electrónico de los agentes. Este correo se forma con la primera letra del nombre seguido del apellido
#y el dominio "@ingenieria.edu.ar"
archi=open("personal.txt")
info=archi.readlines()
corte=[]
nombres=[]
apellido=[]
for i in range(0,len(info)):
    corte.append(info[i].split())
    nombres.append(str(corte[i][0]))
    apellido.append(str(corte[i][1]))
mails=[]
for i in range(len(apellido)):
    email=nombres[i][0]+apellido[i]+"@ingenieria.edu.ar"
    mails.append(email.lower())
    
print(mails)

archivo_correos=open("correos.txt", 'w')
archivo_correos.write(str(mails)+"\n")

archi.close()
archivo_correos.close()