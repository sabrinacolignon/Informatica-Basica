# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:35:17 2022

@author: Sabrina
"""

edad=int(input("ingrese edad del cliente: "))
if edad<4:
    print("el cliente no debe abonar entrada.")
elif edad>=4 and edad<=18:
    print("el cliente debe abonar $150 de entrada.")
else:
    print("el cliente debe abonar $250 de entrada.")