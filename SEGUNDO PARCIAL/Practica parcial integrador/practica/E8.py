# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:51:26 2022

@author: Sabrina
"""

# Escriba el código C++ de la función int intercambia(char *c1), la cual recibe una cadena c1 como parámetro e invierte las
# subcadenas ubicadas antes y después del ter espacio en blanco lo hubiera) y devuelve un entero con la posición del 1er
# espacio en blanco a partir del cual intercambiaron las subcadenas. Ejemplo: si c1 contiene el cstring "Julio Alvez",
# luego de aplicar la función c1 contiene "Alvez Julio". Si c1 no tiene espacio, la función devuelve -1 y no altera la
# cadena.

cadena="julio alvez"
for i in range(len(cadena)):
        if " " in cadena[i]:
            cadena_sep=cadena.split(" ")
            cadena_nueva= cadena_sep[1]+ " "+ cadena_sep[0]
print(cadena_nueva)