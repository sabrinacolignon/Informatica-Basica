# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:01:42 2022

@author: Sabrina
"""

# El archivo PALABRAS.TXT contiene una lista de palabras (una x línea) en singular. Reescriba el archivo pasando
# todas las palabras al plural, agregando “s” si termina en vocal o “es” si termina en consonante.

archivo=open("palabras.txt", "r+")
listado=archivo.readlines()
archivo.seek(0)
for palabra in listado:
    palabra=palabra.rstrip('\n')
    if palabra[-1] in "aeiou":
        palabra=palabra+'s'+'\n'
        archivo.write(str(palabra))
    else:
        palabra=palabra+'es'+'\n'
        archivo.write(str(palabra))
archivo.close()