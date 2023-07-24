# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:05:45 2022

@author: Sabrina
"""

#fecha aaaammdd
fecha=20220531
# anio=fecha//10000
# mes=(fecha%10000)//100
# dia=fecha%100
# print(fecha)
# print(anio, "/", mes, "/", dia)

#fecha ddmmaaaa
fecha="31/05/2022"
# anio=fecha%10000
# mes=(fecha//10000)%100
# dia=fecha//1000000
# print(anio, "/", mes, "/", dia)

fecha=fecha.split('/')
mes=fecha[1]
anio=fecha[2]
print(anio, "/", mes, "/")