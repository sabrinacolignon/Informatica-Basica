# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:18:49 2022

@author: Sabrina
"""
#recibir por parte del usuario la fecha como un número entero en formato aaaammdd 
#y muestre por pantalla: “La fecha es: dd del mm de aaaa"

fecha= int(input("ingrese la fecha en formato aaaammdd: "))
anio= fecha//10000
mes= (fecha%10000)//100
dia= fecha%100

print("la fecha es: ", dia," de ",mes," de: ", anio)