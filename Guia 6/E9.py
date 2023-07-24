# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:05:09 2022

@author: Sabrina
"""

#E9: Una empresa distribuidora de equipos médicos vende 10 artículos distintos y exporta a otros países.
#Posee 3 sucursales y desea analizar el desempeño de las mismas en el 2020.
#Para ello se ingresan 4 datos por cada operación de venta realizada en  ese año: mes (1..12), sucursal(1..8),
#moneda (‘U’ o ‘P’), monto. El dato moneda indica si el monto de la operación es en dólares (‘U’) o en pesos (‘P’). 
#Puede haber varias ventas en un mismo mes y para una misma sucursal.
#a) Organice la información ingresada acumulando por separado los montos vendidos en pesos y en dólares.
#b) Determine la recaudación anual en USD  y en pesos de la sucursal 7.
#c) En el mes de mayo, cuál fue la mayor recaudación en dólares de una sucursal? Y qué sucursal lo logró?
#Use funciones para los puntos b y c.

def recaudacion_anual (lista, sucursal):
    acum=0
    for i in range(len(lista)):
        acum=acum+(lista[i][sucursal])
    return acum
def mayor_recaudacion(lista, mes):
    mayor_rec=lista[mes-1][0]
    suc_mayor_rec=0
    for i in range(len(lista)):
        if mayor_rec>lista[mes-1][i]:
            mayor_rec=lista[mes-1][i]
            suc_mayor_rec=i
    return mayor_rec, suc_mayor_rec

ventas_dolares=[[0]*12 for i in range(8)]
ventas_pesos=[[0]*12 for i in range(8)]

suc=int(input("ingrese sucursal de la venta (para cortar ingrese 0) : "))
while suc!=0:
    mes=int(input("ingrese mes de la venta: "))
    moneda=input("ingrese si el monto de la operación es en dólares (‘U’) o en pesos (‘P’): ")
    if moneda=='U' or moneda=='u':
        monto=int(input("ingrese monto de la venta: "))
        ventas_dolares[suc-1][mes-1].append(monto)
    else:
        monto=int(input("ingrese monto de la venta: "))
        ventas_pesos[suc-1][mes-1].append(monto)      
    suc=int(input("ingrese sucursal de la venta (para cortar ingrese 0) : "))

#la recaudación anual en USD  y en pesos de la sucursal 7:
print("La recaudacion anual de la sucursal 7 en dolares fue: ", recaudacion_anual(ventas_dolares, 7), "dolares.")
print("La recaudacion anual de la sucursal 7 en pesos fue: ", recaudacion_anual(ventas_pesos, 7), "pesos.")

#c) En el mes de mayo, cuál fue la mayor recaudación en dólares de una sucursal? Y qué sucursal lo logró?
print("La mayor recaudacion en dolares del mes de mayo fue de: ", mayor_recaudacion(ventas_dolares, 5))
