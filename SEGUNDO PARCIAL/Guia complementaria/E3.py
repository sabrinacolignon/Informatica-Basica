# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:31:35 2022

@author: Sabrina
"""

#3. Se leen por consola los registros de infectados y fallecidos en el año 2020 de 15 países
#(nombre del país, número infectados, número fallecidos)y se los almacena en una lista.
#a) Calcule e informe el % de mortalidad del país 5 en 2020.
#b) Informe cuántos países tuvieron % de mortalidad superior al 3% en 2020 y los nombres de los mismos.
#c) Calcule e informe el total de muertes de todo 2020.

cantidad_paises=6#15
registro_paises=[]
for i in range(cantidad_paises):
        nombre=input("Ingresar el nombre del pais:")
        n_infectados=int(input("Ingrese el numero de infectados:"))
        n_fallecidos=int(input("Ingrese el numero de fallecidos:"))
        registro_paises.append((nombre, n_infectados, n_fallecidos))

total_muertes=0
for i in range(cantidad_paises):
    total_muertes+=registro_paises[i][2]
    mortalidad_pais_5=round(((registro_paises[4][2]/total_muertes)*100),1)
print('la mortalidad del pais 5',registro_paises[4][0],'es de: ',mortalidad_pais_5,'%')

mortalidad_superior=[]
contador=0
for i in range(cantidad_paises):
    mortalidad=round((registro_paises[i][2]/total_muertes)/100, 1)
    if mortalidad>3:
        mortalidad_superior.append(registro_paises[i][0])
        contador+=1
        print("hubo ", contador, " paises cuyo % de mortalidad supero el 3%")
        print("los paises fueron: ")
        for i in mortalidad_superior:
            print(i)
    else:
        print("no hubo paises con un % de mortalidad mayor al 3%")

suma=0
for i in range(cantidad_paises):
    suma+=registro_paises[i][2]
print("la cantidad de fallecidos de todo el 2020 es de: ", suma, "personas.")
