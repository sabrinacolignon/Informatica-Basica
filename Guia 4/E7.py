# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:54:10 2022

@author: Sabrina
"""
#Escriba un programa que genere al azar 1000 coordenadas en el plano con valores de "x" comprendidos entre -50 y 100, 
#y valores de "y" comprendidos entre -10 y 25. Posteriormente el programa debe solicitar las coordenadas del centro
#y el valor del radio de una circunferencia e indicar cuántos de los puntos del plano se encuentran dentro de la 
#circunferencia. Se recuerda que un punto está fuera, dentro o sobre la circunferencia según sea la 
#relación entre el radio y la distancia entre el punto y el centro de la circunferencia.

"""
#lista por comprension:
#coord=[expresion for variable in rango]
coord=[r.random() for x in range(10)]
    """
import random as r
import math as m

#lista de listas para generar las mil coordenadas en el plano:
coord=[[r.uniform(-50,100), r.uniform(-10,25)] for x in range (10)]#la expresion pasa a ser una lista

radio=float(input("ingrese valor del radio de la circunferencia: "))

centro=[float(input("introduzca coordenadas X del centro: ")), float(input("introduzca coordenadas Y del centro: "))]
cant_dentro=0
#cuando me interesa el subindice
"""for i in range (10):
    d= m.sqrt( ((coord[i][0]- centro[0])**2) + ((coord[i][1]- centro[1])**2)) #trabajo con subindices
    if d<radio:
        cant_dentro+=1
        print("las coordenadas que ingresan a la circunferencia son: ", coord[i])
print("la cantidad de puntos en el plano dentro de la circunferencia son: ", cant_dentro)"""

#cuando me interesa los valores de adentro
 #utilizando a i como una lista que esta dentro de coord
for i in coord:
    d= m.sqrt( ((i[0]-centro[0])**2) + ((i[1]-centro[1])**2)) #no lo manejo como una matriz, cada uno de los elementros de la fila es la variable que se va modificando
    if d<radio:
        cant_dentro+=1
        print("las coordenadas que ingresan a la circunferencia son: ", i)
print("la cantidad de puntos en el plano dentro de la circunferencia son: ", cant_dentro) 