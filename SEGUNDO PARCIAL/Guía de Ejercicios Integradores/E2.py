# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:06:45 2022

@author: Sabrina
"""

# En el archivo “stock.txt” se encuentra almacenado la cantidad de insumos de un almacén de un importante sanatorio
# de la ciudad. Cada línea contiene 5 datos separados por espacio: código de artículo (número entero entre 1000 y
# 1800), cantidad de unidades disponible (número entero), fecha de compra (dd/mm/aaaa), fecha de vencimiento
# (dd/mm/aaaa), descripción del artículo (string). Por otro lado, el archivo “consumos.txt” contiene los pedido
# de insumos que se fueron realizando al almacén durante el día. Cada línea del archivo contiene 3 datos separados
# por espacio: código de artículo (número entero entre 1000 y 1800), cantidad de unidades requeridas
# (número entero), hora en la que se hizo el pedido (hh:mm:ss), los datos de este archivo están ordenados
# cronológicamente. 
# a-  Determine cuántos insumos quedaron en stock al final del día.          
# b- Determine qué insumos  fueron requeridos y no pudieron ser entregados por falta de stock o insumo vencido y cuántas veces pasó esto con cada insumo.
# c- Determine a qué hora comenzaron los pedidos al almacén y a qué hora cesaron.
# d- ¿A qué hora comenzó a quedarse sin insumos el almacén?
# e- Genere el archivo “compras.txt”, el cual contiene 3 datos por línea: código de artículo (número entero entre
# 1000 y 1800), cantidad de unidades a comprar (número entero), descripción del artículo (string). Dicho archivo
# debe indicar cuánto se debe comprar de cada artículo para volver a tener el stock del inicio del día y en el
# caso de los insumos que faltaron, sumarle la cantidad de veces que fue requerido y no pudo ser entregado,
# también debe reponer los insumos vencidos.

