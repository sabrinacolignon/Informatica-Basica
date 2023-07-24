# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:43:23 2022

@author: Sabrina
"""

#Una empresa distribuidora de equipos médicos vende 10 artículos distintos y exporta a otros países.
#Posee 8 sucursales y desea analizar el desempeño de las mismas en el 2020. Para ello se ingresan 4 datos
#por cada operación de venta realizada en  ese año: mes (1..12), sucursal (1..8), moneda (‘U’ o ‘P’), monto.
#El dato moneda indica si el monto de la operación es en dólares (‘U’) o en pesos (‘P’).
#Puede haber varias ventas en un mismo mes y para una misma sucursal.
#a) Organice la información ingresada acumulando por separado los montos vendidos en pesos y en dólares.
#b) Determine la recaudación anual en USD y en pesos de la sucursal 7.
#c) En el mes de mayo, cuál fue la mayor recaudación en dólares de una sucursal? Y qué sucursal lo logró?
#Use funciones para los puntos b y c.

def recaudacion_anual(lista, sucursal):
    acum=0
    for i in range(len(lista)):
        acum+=lista[i][sucursal-1]
    return acum

def mayor_recaudacion(lista, mes):
    suc=0
    mayor=lista[0][0]
    for i in range(len(lista)):
        if mayor<lista[mes-1][i]:
            mayor=lista[mes-1][i]
            suc=i
    return mayor, suc

ventas_pesos=[]
ventas_dolares=[]
mes=int(input("Ingrese mes de la venta: "))
while mes!=0:
    suc=int(input("Ingrese sucursal donde se realizó la venta: "))
    moneda=input("Ingrese moneda en la que se realizo la venta:")
    print("'U' para dolares o 'P' para pesos")
    if moneda=='U' or moneda=='u':
        monto=float(input("Ingrese monto de la venta: "))
        ventas_dolares[mes-1][suc-1].append(monto)
    elif moneda =='P' or moneda=='p':
        monto=float(input("Ingrese monto de la venta: "))
        ventas_pesos[mes-1][suc-1].append(monto)
    else:
        print("No ingresó una moneda correcta")

print("La recaudacion anual en dolares de la sucursal 7 fue de: ", recaudacion_anual(ventas_dolares, 7))
print("La recaudacion anual en pesos de la sucursal 7 fue de: ", recaudacion_anual(ventas_pesos, 7))
mayor_rec, suc_mayor_rec=mayor_recaudacion(ventas_dolares, 5)
print("En el mes de mayo, la mayor recaudacion en dolares fue de: ", mayor_rec, "en la sucursal ", suc_mayor_rec)