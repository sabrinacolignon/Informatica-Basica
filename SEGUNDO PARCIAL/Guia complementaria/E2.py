# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:30:10 2022

@author: Sabrina
"""

#2. Escriba un programa que lea por consola el stock de cada uno de los 10 productos que comercializa una empresa.
#Posteriormente, lea los 16 pares de datos correspondientes a ventas realizadas en la empresa en un día; se leen:
#código y cantidad. Cada vez que lea un par de datos nuevos se debe actualizar el stock y si este no es suficiente
#para realizar la venta se debe informar al usuario el stock disponible de ese producto.
#Una vez finalizada la carga de datos se debe informar al usuario el stock final de cada producto.


cant_productos=2 #10
pares_de_datos=3 #16
stock=[[0]*cant_productos]
for i in range(cant_productos):
    cod=int(input("ingrese codigo de la venta: "))
    stock_ingresado=int(input("ingrese stock de los productos: "))
    stock.append(stock_ingresado)

codigo=[]
cantidad=[]
for j in range(pares_de_datos):
    cod=int(input("ingrese codigo de la venta: "))
    codigo.append(cod)
    cant=int(input("ingrese cantidad de la venta: "))
    cantidad.append(cant)

stock_restado=[[0]*pares_de_datos]
for i in range(pares_de_datos):
    buscar_cod=int(input("ingrese codigo de la venta para revisar stock: "))
    for j in range(cant_productos):
        stock_restado=stock[i]-cantidad.index(cod)[i]
    if cantidad[i]<stock[i]:
        print("el stock no es suficiente, este es de: ", stock[i], "unidades.")
    else:
        print("hay suficiente stock.")

for i in range(cant_productos):
    for j in range(pares_de_datos):
        print("el stock total de cada producto es: ", stock_restado[i][j])