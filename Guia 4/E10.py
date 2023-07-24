# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:03:21 2022

@author: Sabrina
"""

#Una empresa distribuidora comercializa 25 artículos. Posee 4 sucursales y desea analizar el desempeño de las mismas.
#Para ello se ingresan los datos correspondientes a las ventas efectuadas en cierto período:
#código sucursal (1…4), código artículo (1…25), cantidad unidades vendidas. 
#El ingreso de datos finaliza con el código de sucursal 0.
#Determine e informe:
#a. Las cantidades de unidades vendidas por la empresa de cada artículo. 
#b. El total de unidades vendidas por la sucursal 3, sumando todos los artículos. 
#c. La cantidad vendida por la sucursal 1 del artículo 6. 
#d. La sucursal que vendió más unidades del artículo 8.

ventas=[[0]*25 for i in range (4)] #fila=4, columna=25
codigo_suc=int(input("ingrese el codigo de la sucursal: "))
while codigo_suc!=0:
    art=int(input("ingrese articulo: "))
    cant=int(input("ingrese cantidades: "))
    ventas[codigo_suc-1][art-1]+=cant
    codigo_suc=int(input("ingrese el codigo de la sucursal: "))

cantidad_vendidas_suc=[0]*4
cantidad_vendidas_prod=[0]*25
for j in range (4):
    for i in range(25):
        cantidad_vendidas_suc[j]+= ventas[j][i] #elijo en que elemento quiero que se acumule

for i in range (25):
    for j in range(4):
        cantidad_vendidas_prod[i]+= ventas[j][i] #elijo en que elemento quiero que se acumule
print("las cantidades vendidas por cada producto son: ",cantidad_vendidas_prod)

cantidad_suc3= cantidad_vendidas_suc[2] #sumo para la fila 3 todas las columnas
print("el total de unidades vendidas por la sucursal 3 es: ", cantidad_suc3)
    
cantidad_1_6=ventas[0][5] #posicion 0,5
print("la cantidad vendida por la sucursal 1 del articulo 6 es: ", cantidad_1_6)

mayor=ventas[0][7]
for i in range(1,4):
    if mayor<ventas[i][7]:
        mayor=ventas[i][7]
print("la sucursal que vendio mas unidades del articulo 8 es: ", mayor)

