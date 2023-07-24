# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:40:35 2022

@author: Sabrina
"""

#Escriba un programa que permita al usuario leer una cadena de caracteres y exhiba un menú con las opciones:
#Pasar a Mayúsculas
#Pasar a Minúsculas
#Solo la inicial con mayúsculas.
#El programa debe resolver la opción seleccionada por el usuario.
cadena=input("Ingrese cadena de caracteres: ")
print("Ingrese una de las siguientes opciones:")
print("1-Pasar a mayusculas")
print("2-Pasar a minusculas")
print("3-Solo la inicial a mayusculas")
opcion=int(input("Ingrese opcion que desee: "))
if opcion==1:
    n_cadena=cadena.upper()
    print("La nueva cadena es: ",n_cadena)
elif opcion==2:
    n_cadena=cadena.lower()
    print("La nueva cadena es: ", n_cadena)
elif opcion==3:
    n_cadena=cadena.capitalize()
    print("La nueva cadena es: ", n_cadena)
else:
    print("Ninguna de las opciones ingresadas es correcta")