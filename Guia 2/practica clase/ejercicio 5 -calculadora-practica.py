# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:26:37 2022

@author: Sabrina
"""

variable1=float(input("ingrese primer valor: "))
variable2=float(input("ingrese segundo valor: "))
opcion=int(input("ingrese: 1(suma), 2 (resta), 3 (multiplicacion), 4 (division): "))
resultado=0

if variable1>variable2:
   if opcion==1:
      resultado=variable1+variable2
      print("el resultado es: ", resultado)
   elif opcion==2:
       resultado=variable1-variable2
       print("el resultado es: ", resultado)
   elif opcion==3:
       resultado=variable1*variable2
       print("el resultado es: ", resultado)
   elif opcion==4:
       resultado=variable1/variable2
       print("el resultado es: ", resultado)
   else:
       print("la opcion ingresada no es correcta")
else:
    if opcion==1:
       resultado=variable1+variable2
       print("el resultado es: ", resultado)
    elif opcion==2:
        resultado=variable2-variable1
        print("el resultado es: ", resultado)
    elif opcion==3:
        resultado=variable1*variable2
        print("el resultado es: ", resultado)
    elif opcion==4:
        resultado=variable2/variable1
        print("el resultado es: ", resultado)
    else:
        print("la opcion ingresada no es correcta")