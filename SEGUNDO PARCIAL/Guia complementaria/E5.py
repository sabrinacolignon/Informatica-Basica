# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:33:25 2022

@author: Sabrina
"""

# 5. Se ingresan por pantalla los siguientes datos de un grupo de pacientes de un centro médico: Nombre, DNI, Sexo (M o F), 
# Obra Social y edad. Si un paciente no tiene Obra Social se ingresa “---“. Determine e informe: 
#a) El % de mujeres del grupo. 
#b) El número de pacientes menores a 45 años. 
#c) Muestre solo apellido, nombre y DNI de los pacientes cuya obra social es IOSPER.

lista_pacientes=[]
dni=int(input("Ingrese DNI del paciente: "))

while dni!=0:
    nombre=input("Ingrese nombre y apellido del paciente: ")
    sexo=input("Ingrese sexo (f o m): ")
    obra_social=input("Ingrese obra social: ")
    edad=int(input("Ingrese edad: "))
    lista_pacientes.append([dni, nombre, sexo, obra_social, edad])
    print("Si quiere finalizar el ingreso de pacientes, debe introducir un dni igual a 0.")
    dni=int(input("Ingrese DNI del paciente: "))

print("elementos de la lista:", len(lista_pacientes))

contador_f=0
porcentaje_f=0
for i in range(len(lista_pacientes)):
    if lista_pacientes[i][2] =='f':
        contador_f+=1
porcentaje_f= round(contador_f/len(lista_pacientes))*100,2)
print("El % de mujeres del grupo es: ", porcentaje_f)

contador_e=0
for i in range(len(lista_pacientes)):
    if lista_pacientes[4]<45:
        contador_e+=1
print("El numero de pacientes menores a 45 años es de: ", contador_e)

contador_os=0
iosper=0
for i in range(len(lista_pacientes)):
    if lista_pacientes[3]=='iosper':
        contador_os+=1
        iosper=i
        print("Los oaceintes que tienen obra social iosper son:")
        print("Nombre: ", lista_pacientes[i][0],"DNI: ", lista_pacientes[i][1])