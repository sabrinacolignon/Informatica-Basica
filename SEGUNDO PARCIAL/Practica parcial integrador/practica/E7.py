# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:51:14 2022

@author: Sabrina
"""

# La Universidad UNZ realiza servicios de consultoria a diversos organismos publicos y privados a través de sus 9 facultades.
# Se dispone de una archivo SERVICIOS UNZ TXT que contiene en cada linea 4 numeros correspondiente a cada consultoria
# realizada durante 2016: codigo Facultad (1.9). monto del servicio (float), dia (1.31), mes (1.12). Puede haber varios
# servicios en un mismo mes para una Facultad. Organice los montos de cada servicio de consultoria en una tabla o matriz de
# 9 filas x 13 columnas Las primeras 12 columnas corresponden a cada mes de 2016. El programa debe obtener e informar:
#     a) el total recaudado x cada facultad en 2016, indicando esta cifra en la columna 13 de la tabla;
#     b) El mes y monto de mayor ingreso en la UNZ considerando todas las facultades,
#     c) en cuantos meses la facultad 4 no tuvo ingresos por servicios de consultoría?.
#     El programa debe emplear las funciones para resolver los items a, b y solicitados.  