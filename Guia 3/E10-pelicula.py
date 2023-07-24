# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:28:05 2022

@author: Sabrina
"""

#Una película ha costado 150 millones de dólares. La primera semana, la película tiene
#un costo de 31 millones de dólares. Cada semana que pasa, la factura es el 20% inferior
#a la de la semana anterior.
#Escriba un programa que indique el número de semanas que se puede permitir la
#película para su producción

costo_inicial=int(input("ingrese costo inicial de la pelicula: $"))
costo_primerS=int(input("ingrese el costo de la primer semana: $"))
contador_semanas=0
porcentaje_restado=((costo_primerS*20)/100)

while costo_primerS<=costo_inicial:
    costo_semanal=costo_primerS+porcentaje_restado
    contador_semanas+=1
    print("las semanas son: ", contador_semanas)
    
print("la cantidad de semanas que se puede permitir la pelicula para su produccion es: ", contador_semanas)