# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:25:18 2022

@author: fmasa
"""

import random as r

nu=["A","C","G","T"]

sec=[]
for i in range(5000):
    sec.append(nu[r.randint(0,3)])

#proporcion de nucleotidos
pA = (sec.count(nu[0])/len(sec))*100
pC = (sec.count(nu[1])/len(sec))*100
pG = (sec.count(nu[2])/len(sec))*100
pT = (sec.count(nu[3])/len(sec))*100
print("La proporcion de A es", pA,"%")
print("La proporcion de C es", pC,"%")
print("La proporcion de G es", pG,"%")
print("La proporcion de T es", pT,"%")
#Cantidad que aparece el nucleotido t:
tt=sec.count(nu[3])
print("El nucleotido t aparece",tt,"veces")
#Secuencia cg
count_cg=0
for i in range(len(sec)-1) :
    if sec[i] == nu[1] and sec[i+1] == nu[2]:
        count_cg += 1
print("La cantidad de secuencias CG es", count_cg)