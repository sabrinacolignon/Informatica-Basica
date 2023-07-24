# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:14:16 2022

@author: Sabrina
"""

# El archivo PALABRAS.TXT contiene una lista de palabras (una x línea) en singular. Reescriba el archivo
# pasando todas las palabras al plural, agregando “s” si termina en vocal o “es” si termina en consonante.
with open ("palabras.txt", "r+") as archivo:
    palabras=archivo.readlines()
    archivo.seek(0)
    for palabra in palabras:
        palabra=palabra.rstrip('\n')
        if palabra[-1] in "aeiou":
            palabra_c=palabra+"s"
            archivo.write(str(palabra_c)+'\n')
        else:
            palabra_c=palabra+"es"
            archivo.write(str(palabra_c)+'\n')
