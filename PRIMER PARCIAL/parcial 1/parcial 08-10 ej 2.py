# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:07:52 2022

@author: Sabrina
"""
lista_mes=[]
ventas=[[0]*12 for i in range(8)]
mes=int(input("ingrese n mes de la venta: "))
while mes!=0:
    cod_suc=int(input("ingerse codigo de la sucursal"))
    cant=int(input("ingrese cantidad vendida: "))
    for i in range(len(ventas)*8):
        ventas[lista_mes.index(mes)][cod_suc-1]=cant
    mes=int(input("ingrese n mes de la venta: "))

cant_vendidas_suc=[]*8
cant_vendidas_prod=[]*12
for i in range(8):
    for j in range(12):
        cant_vendidas_suc[i]+=ventas[i][j]
for j in range(12):
    for i in range(8):
        cant_vendidas_prod[j]+=ventas[i][j]        

print("el total vendido por la sucursal 3 en todo el año es: ", cant_vendidas_suc[2])
print("el total vendido por todas las sucursales vendidas en mayo: ", cant_vendidas_prod[4])
