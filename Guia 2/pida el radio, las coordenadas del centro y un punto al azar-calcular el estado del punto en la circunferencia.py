# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:18:41 2022

@author: Sabrina
"""
#Escriba un programa que pida el radio, las coordenadas del centro de una
#circunferencia y las coordenadas de un punto y que indique si el punto está sobre la
#circunferencia, dentro o fuera de ella.
#Se recuerda que un punto está fuera, dentro o sobre la circunferencia según sea la
#relación entre el radio y la distancia entre el punto y el centro de la circunferencia.

radio=float(input("ingrese el radio de la circunferencia: "))
centro_circunferencia_x=float(input("ingrese las coordenadas en x del centro de una circunferencia: "))
centro_circunferencia_y=float(input("ingrese las coordenadas en y del centro de una circunferencia: "))

punto_aleatorio_x=float(input("ingrese las coordenadas en x de un punto: "))
punto_aleatorio_y=float(input("ingrese las coordenadas en y de un punto: "))

distancia_puntos_x= (punto_aleatorio_x-centro_circunferencia_x)**2
distancia_puntos_y= (punto_aleatorio_y-centro_circunferencia_y)**2
distancia=(distancia_puntos_x+distancia_puntos_y)**(1/2)

if distancia<radio:
    print("el punto esta dentro de la circunferencia")
elif distancia==radio:
    print("el punto esta sobre la circunferencia")
else:
    distancia>radio
    print("el punto esta por fuera de la circunferencia")