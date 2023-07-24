# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:28:14 2022

@author: fmasa
"""

import random as r
x=[]
for i in range(1000):
    x.append(round(r.random(),2))
resultado=[]
for j in range(len(x)):
    a=x.count(x[j])
    resultado.append([x[j],a])
print(resultado)
    
      
    