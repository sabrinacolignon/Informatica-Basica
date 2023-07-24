# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:52:20 2022

@author: Sabrina
"""

# El archivo PALABRAS.TXT contiene una lista de palabras (una x línea) en singular. Reescriba el archivo
# pasando todas las palabras al plural, agregando “s” si termina en vocal o “es” si termina en consonante.

with open("palabra.txt", "r+") as archivo:
    palabras=archivo.readlines()
    archivo.seek(0)
    for palabra in palabras:
        palabra=palabra.rstrip('\n')
        if palabra[-1] in "aeiou":
            palabra=palabra+"s"+"\n"
            archivo.write(palabra)
        else:
            palabra=palabra+"es"+"\n"
            archivo.write(palabra)