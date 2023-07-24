# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:20:58 2022

@author: Sabrina
"""

#10. Una empresa distribuidora comercializa 25 artículos. Posee 4 sucursales y desea analizar el desempeño
#de las mismas. Para ello se ingresan los datos correspondientes a las ventas efectuadas en cierto período:
#código sucursal (1…4), código artículo (1…25), cantidad unidades vendidas.
#El ingreso de datos finaliza con el código de sucursal 0.
#Determine e informe:
#a. Las cantidades de unidades vendidas por la empresa de cada artículo. 
#b. El total de unidades vendidas por la sucursal 3, sumando todos los artículos. 
#c. La cantidad vendida por la sucursal 1 del artículo 6. 
#d. La sucursal que vendió más unidades del artículo 8.

ventas=[[0]*24 for i in range(4)]
cod_suc=int(input("ingrese codigo de la sucursal: "))
while cod_suc!=0:
    art=int(input("ingrese articulo: "))
    cant=int(input("ingrese cantidad de articulos vendidos: "))
    ventas[cod_suc-1][art-1]=cant
    cod_suc=int(input("ingrese codigo de la sucursal: "))

cantidad_vend_suc=[]*4
cantidad_vend_art=[]*24
for i in range(24):
    for j in range(4):
        cantidad_vend_art[i]=ventas[i][j]
for j in range(4):
    for i in range(24):
        cantidad_vend_suc[j]=ventas[i][j]

print("las cantidades vendidas por cada articulo son: ", cantidad_vend_art)

cant_suc_3=cantidad_vend_suc[2]
print("el total de unidades vendidad por la sucursal 3 es: ", cant_suc_3)

cant_1_6=ventas[0][5]
print("la cantidad vendida por la sucursal 1 del articulo 6 es: ", cant_1_6)

mayor=ventas[0][0]
for i in range(1,4):
    if mayor<ventas[i][7]:
        mayor=ventas[i][7]
print("La sucursal que vendió más unidades del artículo 8 es: ", mayor)