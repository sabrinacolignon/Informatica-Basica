# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:57:01 2022

@author: Sabrina
"""

with open ("ECG.txt", "r") as archivo:
    ecg=archivo.readlines()

#map(funcion, iterable)-> duvuelve un iterador que le vamos a decir que lo haga una lista y a eso lo almacenamos en una lista convertida. la funcion puede ser cualquier cosa.
#Agarra el primer dato, lo pasa como parametro y lo quee sta devuelva lo pone como primer elemnto de esa lista, como el primer elemento de la otra lista
#reemplaza el for
ecg=list(map(int,ecg))#->forma mas facil de leer un archivo si es solo un vector de numeros de mismo tipo
promedio=sum(ecg)/len(ecg)
umbral=20*promedio
contador=0
for señal in ecg:
    if señal>umbral:
        contador+=1
print(contador, "fue la cantidad de valores que superan en umbral.")
    