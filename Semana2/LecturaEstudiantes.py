# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:36:19 2022

@author: ailen
"""
import Estudiante

with open("alumnos.txt") as arch:
        lista_alumnos = list(arch)
        

datos = list()
for linea in lista_alumnos:
    datos.append(linea.split(","))
    
print(datos)

for linea in datos:
    estudiantes= Estudiante()