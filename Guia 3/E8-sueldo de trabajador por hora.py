# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:53:37 2022

@author: Sabrina
"""
import random as r
#Una Empresa paga a sus 100 operarios semanalmente de acuerdo con la cantidad de
#horas trabajadas, a razón de X pesos la hora hasta 40 hs. y un 50% más por todas las
#horas que pasan de 40. Informar el total de salario a cobrar por cada trabajador.

cantidad_operarios=100
sueldo_hora=float(input("ingrese el sueldo por hora: $"))
for operario in range(0, 5):
    horas_op=r.randint (0,45)
    if horas_op<=40:
        sueldo=sueldo_hora*horas_op
        print("sueldo del operario", operario + 1," : $", sueldo)
    else:
        sueldo=sueldo_hora*((horas_op*50)/100)
        print("el sueldo de cada trabajador es: $", sueldo)
    
