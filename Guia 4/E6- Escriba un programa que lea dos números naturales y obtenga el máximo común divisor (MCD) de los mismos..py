# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:51:31 2022

@author: Sabrina
"""

# Escriba un programa que lea dos números naturales y obtenga el máximo común divisor (MCD) de los mismos.
numero1=int(input("Ingrese primer numero: "))
numero2=int(input("Ingrese segundo numero: "))
mcd=1 #uno porque es generalmente el mcd de dos numeros cuando no se encuentra otro numero mayor qeue este

divisores_n1=[]
for i in range(2, numero1+1):
    if numero1%i==0:
        divisores_n1.append(i)

divisores_n2=[]
for i in range(2, numero2+1):
    if numero2%i==0:
        divisores_n2.append(i)
div_comunes=[]
for i in divisores_n1:
    if i in divisores_n2:
        div_comunes.append(i)

for i in div_comunes:
    if div_comunes[i]==1:
        print("El Máximo Comun Divisor es 1.")
    else:
        maximo=max(div_comunes)
        print("El Máximo Comun Divisor es: ", maximo)
                
        
        
