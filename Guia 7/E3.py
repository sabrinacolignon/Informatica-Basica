# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:06:07 2022

@author: Sabrina
"""

#Escriba un programa que permita al usuario leer una cadena de caracteres y exhiba un menú con las opciones:
#Pasar a Mayúsculas
#Pasar a Minúsculas
#Solo la inicial con mayúsculas.
#El programa debe resolver la opción seleccionada por el usuario.


cadena=input("ingrese cadena de caracteres: ")
print("Ingrese una de las siguientes opciones")
print("1- Pasar a mayúsculas")
print("2-Pasar a minúsculas")
print("3-Solo la inicial con mayúsculas")

opcion=int(input("Ingrese su opcion: "))

if opcion==1:
    nueva_c=cadena.upper()
    print("La nueva cadena es: ", nueva_c)
elif opcion==2:
    nueva_c=cadena.lower()
    print("La nueva cadena es: ", nueva_c)
elif opcion==3:
    nueva_c=cadena.capitalize()
    print("La nueva cadena es: ", nueva_c)
else:
    print("no ingresó una opcion correcta.")
    