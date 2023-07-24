# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:44:23 2022

@author: Sabrina
"""
#Una asociación cooperadora escolar recibe aportes de dinero variable de los estudiantes asociados. 
#Se leen sin orden alguno los montos aportados en el último año y la fecha correspondiente (día, mes).
#Estos datos terminan con el valor de monto cero. Informe:
#a. el total recaudado por mes. 
#b. El mes de menor aporte. 
#Para resolver el problema organice los datos en una lista de 12 elementos.

aportes=[0]*12
monto=float(input("ingrese monto del aporte del alumno: "))
total_recaudado=0#uso sum

while monto!=0:
        dia=int(input("ingrese dia del aporte del alumno: "))
        mes=int(input("ingrese mes del aporte del alumno: "))
        aportes[mes-1]=monto
        monto=float(input("ingrese monto del aporte del alumno: "))

for i in range(12):
    total_recaudado=sum(aportes)

menor_aporte=aportes[0][0]        
for i in range(12):
    if aportes[1][i]<menor_aporte:
        menor_aporte=aportes[1][i]
            
print("la lista de aportes es: ", aportes)
print("el total recaudado por mes es: ", total_recaudado)
print("el mes de menor aporte es: ", menor_aporte)
            