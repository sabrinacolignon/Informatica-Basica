# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:33:55 2022

@author: Sabrina
"""

#6. Se ingresan por pantalla las coordenadas x, y, z del recorrido de un alpinista tomadas cada 15 segundos mientras
#escala una montaña. El ingreso de datos finaliza con la terna [0, 0, 0]. Almacene los datos en una lista y determine: 
#a) La cantidad de veces que el alpinista debió descender para sortear algún obstáculo. 
#b) La amplitud del desplazamiento en x (Max “x” – Min “x”). 
#c) El tiempo total empleado en el ascenso. 
#d) El tiempo de descanso del alpinista.

x=int(input("ingrese coordenadas x del recorrido: "))
y=int(input("ingrese coordenadas y del recorrido: "))
z=int(input("ingrese coordenadas z del recorrido: "))
terna=[]*3
while x!=0 and y!=0 and z!=0:
        terna.append([x,y,z])
        x=int(input("ingrese coordenadas x del recorrido: "))
        y=int(input("ingrese coordenadas y del recorrido: "))
        z=int(input("ingrese coordenadas z del recorrido: "))
obstaculo=0
for i in range(len(terna)):
    if terna[i,i,0]>terna[i,i,1]:
        obstaculo+=1

#a: cuando z (altura) va aumentadno y de la nada desciende, quiere decir que la persona tuvo un obstaculo
#c: 15 segundos*largo de la lista de coordenadas
#d: 15*cuantas veces tengo 2 datos repetidos