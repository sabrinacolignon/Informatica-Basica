# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:27:51 2022

@author: Sabrina
"""

#Un grupo de investigación analiza el comportamiento de 65 pacientes hospitalizados y afectados por COVID19.
#Para ello se ingresan el número de paciente y luego los valores de presión de oxígeno en sangre registrados
#para ese paciente durante 7 días (una medición por día).
#a) Almacene la información ingresada en una lista.
#b) Calcule mediante una función  cuántos pacientes tuvieron hipoxemia (presión de oxígeno
#inferior a 72) durante 2 o más días. Escriba el programa en Python que calcule e informe los resultados.
import random as r

def hipoxemia(lista):
    cont=0
    for i in range(65):
        for j in range(2, 7):
            if lista[i][j]<72:#IndexError: list index out of range
                cont+=1
    return cont

pacientes=[]
for i in range (65):
    presion_ox=[]
    for j in range(7):
        dato=r.randint(1,100)
        presion_ox.append(dato)
    pacientes.append(presion_ox)
    
print("la cantidad pacientes tuvieron hipoxemia (presión de oxígeno inferior a 72) durante 2 o más días fueron:")
print(hipoxemia(pacientes))