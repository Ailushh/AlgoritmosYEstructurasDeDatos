# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:34:21 2022

@author: ailen
"""

class Estudiante:
    
    def __init__(self, legajo=0, apellido ='NN', nombre ='NN', DNI = 0, promedio = 0):
        self._legajo = legajo
        self._DNI = DNI
        self._apellido = apellido
        self._nombre = nombre
        self._promedio = promedio
        
    @property
    def legajo(self):
        return self._legajo
    
    @legajo.setter
    def legajo(self, valor):
        self._legajo = valor
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, palabra):
        self._apellido = palabra
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, palabra):
        self._nombre = palabra
    
    @property
    def DNI(self):
        return self._DNI
    
    @DNI.setter
    def DNI(self, valor):
        self._DNI = valor
        
    @property
    def promedio(self):
        return self._promedio
    
    @promedio.setter
    def promedio(self, valor):
        self._promedio = valor
        
if __name__ == "__main__":
   
   alumno1 = Estudiante(452, "Blanch", "Federico", 38544890, 7.5)
   print(alumno1.DNI)
   print(alumno1.apellido)
   print(alumno1.nombre)
   print(alumno1.legajo)
   print(alumno1.promedio)
        
    