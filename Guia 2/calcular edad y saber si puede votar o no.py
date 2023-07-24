# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:47:10 2022

@author: Sabrina
"""

#Deseamos saber si un estudiante de colegio secundario
#vota en las próximas elecciones legislativas a llevarse a
#cabo el próximo 24 de octubre, para ello debe ser mayor de
#16 años. Escriba un programa en Python donde se ingrese la fecha de nacimiento del
#estudiante con formato día, mes, año y se informe si vota o no.
edad_anios=int(input("ingrese el año de nacimiento del estudiante: "))
edad_meses=int(input("ingrese el mes de nacimiento del estudiante: "))
edad_dia=int(input("ingrese el dia de nacimiento del estudiante: "))
fecha_votacion_dia=24
fecha_votacion_mes=10
fecha_votacion_ano=2022
edad= fecha_votacion_ano-edad_anios

if edad_dia<=fecha_votacion_dia and edad_meses<=fecha_votacion_mes and edad<16:
    print("el estudiante no puede votar.")
else:
    edad_dia>fecha_votacion_dia and edad_meses>=fecha_votacion_mes and edad>=16
    print("el estudiante puede votar")
