# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:06:12 2022

@author: Sabrina
"""
#Pedir al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal 
#y lo almacene en una variable, y muestre por pantalla la frase "Tu índice de masa corporal es <imc>"
#donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
#IMC=peso/(altura*altura)
peso= float (input("ingrese su peso en kg: "))
altura= float(input("ingrese su estatura en metros: "))
imc=peso/(altura**2)
print("Tu indice de masa corporal (imc) es: ", round(imc,2))