# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:56:51 2022

@author: Sabrina
"""

radio=float(input("ingrese el radio de la circunferencia: "))
coordenadasc_x=float(input("ingrese coordenadas en x de la circunferencia: "))
coordenadasc_y=float(input("ingrese coordenadas en y de la circunferencia: "))
punto_x=float(input("ingrese coordenadas en x del punto: "))
punto_y=float(input("ingrese coordenadas en y del punto: "))
distancia_x=(coordenadasc_x-punto_x)**2
distancia_y=(coordenadasc_y-punto_y)**2
suma=distancia_x+distancia_y
raiz=(suma)**(1/2)
if raiz==radio:
    print("el punto esta sobre la circunferencia.")
elif raiz<radio:
    print("el punto esta dentro de la circunferencia.")
elif raiz>radio:
    print("el punto esta por fuera de la circunferencia.")
else:
    print("los datos ingresados no son correctos.")
