# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 18:48:01 2022

@author: Sabrina
"""

#anota el kilometraje que marca el odómetro justo antes de iniciar el
#viaje, y toma nota nuevamente justo al llegar a destino. Conoce además el consumo de
#nafta del vehículo en ruta (es decir, cuantos litros gasta en promedio por cada kilómetro
#recorrido), y el precio del litro de nafta. Escriba un algoritmo para calcular el costo de un viaje

kilometraje_inicial= float (input("ingrese kilometraje que marca el auto al iniciar el viaje "))
kilometraje_final= float (input("ingrese kilometraje que marca el auto al finalizar el viaje "))
consumo_por_litro= float(input("ingrese el consumo de nafta del auto "))
precio_nafta= float(input("ingrese el precio de la nafta "))
descuento_por_cliente= float(input("ingrese el descuento por ser cliente "))

kilometros_recorridos=(kilometraje_final-kilometraje_inicial)
consumo_nafta=kilometros_recorridos*consumo_por_litro
valor_final_nafta=precio_nafta-(precio_nafta*(descuento_por_cliente/100))
costo_del_viaje= consumo_nafta*valor_final_nafta


print("el costo del viaje es de $ ", costo_del_viaje)