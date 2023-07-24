# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 03:04:51 2022

@author: yamil
"""

'''3. Se leen por consola los registros de infectados y fallecidos en el año 
2020 de 15 países (nombre del país, número infectados, número fallecidos) y 
se los almacena en una lista.

a) Calcule e informe el % de mortalidad del país 5 en 2020.

b) Informe cuántos países tuvieron % de mortalidad superior al 3% en 2020
   y los nombres de los mismos.

c) Calcule e informe el total de muertes de todo 2020. '''

registros=[]
for i in range(15):
    pais=input('pais:')
    infectados=int(input('numero de infectados:'))
    fallecidos=int(input('numero de fallecidos:'))
    x=(pais,infectados,fallecidos)
    registros.append(x)

mortalidad_total=0

for i in range(15):
    mortalidad_total=registros[i][2]+mortalidad_total
mortp5=round(((registros[4][2]/mortalidad_total)*100),1)
print('la mortalidad del pais 5',registros[4][0],'es',mortp5,'%')

mort_sup_3=[]
cant_mort_sup_3=0
for i in range(15):
    mort=round(((registros[i][2]/mortalidad_total)*100),1)
    if mort>3:
        mort_sup_3.append(registros[i][0])
        cant_mort_sup_3=cant_mort_sup_3+1
print(cant_mort_sup_3,'paises con mortalidad superior al 3%')
for i in mort_sup_3:
    print(i)

suma=0
for i in range(15):
    suma=registros[i][2]+suma
print('el total de muertes en 2020 es:',suma)

