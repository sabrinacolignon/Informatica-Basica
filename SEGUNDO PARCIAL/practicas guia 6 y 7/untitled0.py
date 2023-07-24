# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:42:49 2022

@author: Sabrina
"""

#Un grupo de investigación analiza el comportamiento de 65 pacientes hospitalizados y afectados por COVID19.
#Para ello se ingresan el número de paciente y luego los valores de presión de oxígeno en sangre registrados
#para ese paciente durante 7 días (una medición por día).
#a) Almacene la información ingresada en una lista.
#b) Calcule mediante una función  cuántos pacientes tuvieron hipoxemia (presión de oxígeno inferior a 72)
#durante 2 o más días. Escriba el programa en Python que calcule e informe los resultados.
import random as r

def tuvieron_hipoxemia(lista, cantidad_pacientes, dias_mediciones):
    contador=0
    for i in range(cantidad_pacientes):
        for j in range(2,dias_mediciones):
            if lista[i][j]<=72:
                contador+=1
    return contador

pacientes=[]
for i in range(65):
    oxigeno=[]
    for j in range(7):
        #mediciones=int(input("Ingrese mediciones del paciente: "))
        mediciones=r.randint(10, 100)
        oxigeno.append(mediciones)
    pacientes.append(oxigeno)

print("La cantidad de pacientes que padecieron de hipoxima fueron: ", tuvieron_hipoxemia(pacientes, 65,7))