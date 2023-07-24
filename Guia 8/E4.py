# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:19:17 2022

@author: Sabrina
"""

#El archivo PALABRAS.TXT contiene una lista de palabras (una x línea) en singular. Reescriba el archivo pasando todas
#las palabras al plural, agregando “s” si termina en vocal o “es” si termina en consonante.
archi=open ("PALABRAS.txt", 'r+')
info=archi.readlines()
archi.seek(0)
for palabra in info:
    palabra=palabra.rstrip('\n')
    if palabra[-1] in "aeiou":      
        palabra_completa=str(palabra+'s'+'\n')
        archi.write(palabra_completa)
    else:
        palabra_completa=str(palabra+'es'+'\n')
        archi.write(palabra_completa)
        
archi.close()